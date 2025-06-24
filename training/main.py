#main module of EXIF Predictor package of LensIQ Suite



from exif_analyser import *
from model import preprocess
from visuals import *
import joblib
from sklearn.metrics import mean_squared_error, r2_score


exif_tocsv("/storage/emulated/0/DCIM/Imaging Edge Mobile/", "exif1.csv")

df=pd.read_csv("exif.csv")
df=preprocess(df)

X_ext=df[['Aperture', 'log_ss', 'log_iso', 'sin_time']]
y_ext=df['EV']

loco={"Linear":"linear.pkl", "Lasso":"lasso.pkl", "Ridge":"ridge.pkl"}

for name, loc in loco.items():
	model=joblib.load(loc)
	y_epred=model.predict(X_ext)
	mse=mean_squared_error (y_ext, y_epred)
	r2=r2_score (y_ext, y_epred)
	print(name)
	print("MSE: ", mse)
	print("R² score: ", r2)
	print()
