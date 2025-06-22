#image folder/csv run app of EXIF Predictor package of LensIQ Suite



from img_tocsv import folder_tocsv 
from preprocessing import preprocess
from visuals import *
from ev_map import ev_scene
import joblib
from sklearn.metrics import mean_squared_error, r2_score

folder=input("Enter folder path: ")
save=input("Enter save path: ")
img_count=int(input("Enter no of images to use: "))
folder_tocsv(folder, save, img_count)

df=pd.read_csv(save)
df=preprocess(df)

X_ext=df[['Aperture', 'log_ss', 'log_iso', 'sin_time']]
y_ext=df['EV']

model=joblib.load("ev_predict.pkl")
y_epred=model.predict(X_ext)

df["Predicted EV"]=y_epred
df["Scene"]=df["Predicted EV"].apply(lambda x: ev_scene(x))

print("EV Predictions with mapped Scene ")
print(df[["Predicted EV", "Scene"]])

mse=mean_squared_error (y_ext, y_epred)
r2=r2_score (y_ext, y_epred)
print("MSE: ", mse)
print("R² score: ", r2)

print("Plots for visual analysis: ")
compare_ev(y_ext, y_epred)
residualplot(y_ext, y_epred)
ev_time(df)
ev_features(df)
