#single image run app of EXIF Predictor package of LensIQ Suiteimport numpy as np


import pandas as pd
import joblib
from ev_map import ev_scene
from img_tocsv import singleimg
from preprocessing import preprocess


img_path=input("Enter image path: ")
nd=int(input("Enter ND stops if used: "))

data=singleimg(img_path)
df=pd.DataFrame([data])
df=preprocess(df)
df=df[['Aperture', 'log_ss', 'log_iso', 'sin_time']]

model=joblib.load("linear.pkl")
ev=model.predict(df)[0]

print("Predicted EV: ", ev)
print("Scene: ", ev_scene(ev, nd))