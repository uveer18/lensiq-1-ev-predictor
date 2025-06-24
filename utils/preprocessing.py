import numpy as np

def preprocess(df):
	df = df[(df['Shutter Speed'] > 0) & (df['ISO'] > 0)]
	df['log_ss'] = df['Shutter Speed'].apply(lambda x: np.log2(float(x)))
	df['log_iso']=np.log2(df['ISO'])
	df['hour']=df['Time of Day'].str.split(':').str[0].astype(int)
	df['min']=df['Time of Day'].str.split(':').str[1].astype(int)
	df['sin_time']=np.sin((df['hour'] + df['min']/60) * 2 * np.pi / 24)
	return df