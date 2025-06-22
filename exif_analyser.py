#exif analyser and csv generator module of EXIF Predictor package of LensIQ Suite 


import os
import math
import numpy as np
import pandas as pd
from PIL import Image
from datetime import datetime

def ev_scene(ev, nd_stops=0):
    adjusted_ev = round(ev + nd_stops)
    mapping = {
        -3: "Candlelight (very dim)",
        -2: "Full moonlight",
        -1: "Dim night street",
         0: "Night city w/ lamps",
         1: "Twilight (blue hour)",
         2: "Moody candlelit indoor",
         3: "Bar/restaurant lighting",
         4: "Bright indoor w/ windows",
         5: "Window-lit overcast scene",
         6: "Overcast outdoor",
         7: "Open shade, late evening",
         8: "Cloudy daylight",
         9: "Shade on sunny day",
        10: "Soft daylight",
        11: "Sunny daylight",
        12: "Bright beach or sand",
        13: "Snow in sun",
        14: "Reflective water / mountains",
        15: "Direct noon sun (extreme brightness)"
    }
    return mapping.get(adjusted_ev, f"EV {adjusted_ev} scene not defined")


def exif_tocsv(folder, save, img_count=None):
	
	#defining tags that correlate with image brightness
	brighttags={
		0x9003: "Time of Day",
  	  0x829D: "Aperture",
	    0x829A: "Shutter Speed",
  	  0x8827: "ISO"
	}
	data=[] #collective exif data
	count=0 #counter for no of images 
	
	#accessing images individually 
	for file in os.listdir(folder):
		if file.lower().endswith(('.jpg', '.jpeg', '.png', '.raw')):
			image_path=folder+file
			image=Image.open(image_path)
			exif_data=image._getexif()
			metadata={}
				
			#handling missing exif data
			if exif_data is None:
				print(f"No EXIF found in {file}")
				metadata={tag_name:None for tag_name in brighttags.values()}
				
			#selecting specific exif data when found
			else:
				for tag_id, tag_name in brighttags.items():
					value=exif_data.get(tag_id)
					#converting datetime to time only
					if isinstance(value, str):
					   try:
					   	value=datetime.strptime(value, "%Y:%m:%d %H:%M:%S").strftime("%H:%M")
					   except:
					   	pass
					
					#converting rational values of shutter speed
					if isinstance(value, tuple) and len(value)==2 and value[1]!=0:
						value=round(value[0] / value[1], 2)
					metadata[tag_name]=value
				
				#calculation and insertion of ev
				val=list(metadata.values())
				if None not in val and 0 not in val:
					ev=math.log((100*(val[1]**2))/(val[2]*val[3]), 2)
					metadata["EV"]=ev
					metadata["scene"]=tag_ev(ev)
					#calculation and insertion of brightness
					#gray=image.convert('L')
					#bright=np.asarray(gray).mean()
					#metadata["Brightness"]=bright
				else:
					print(f"Incomplete EXIF found in {file}")
					print(" >File dropped")
					continue
				
			#appending individual image exif
			data.append(metadata)
			
			#increasing counter
			count+=1
			
			#count reached
			if img_count is not None:
				if count==img_count:
					break
				else:
					continue
	#turning list into dataframe
	if count!=0:
	 	df=pd.DataFrame(data)
	 	df.dropna()
	else:
	 	print(f"No usable EXIF found in {folder}")
			
	#exporting to csv
	df.to_csv(save, index=False)
	print(f"EXIF of {'all' if img_count is None else ''} {count} images in {folder} saved to {save}\n")