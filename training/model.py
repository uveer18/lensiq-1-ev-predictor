import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from preprocessing import preprocess

df = pd.read_csv('exif1.csv')

df=preprocess(df)
X = df[['Aperture', 'log_ss', 'log_iso', 'sin_time']] #features
y = df['EV'] #target

X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.005, random_state=42)

models={"Linear": LinearRegression(),"Lasso":Lasso(), "Ridge":Ridge()}
loc=["linear.pkl", "lasso.pkl", "ridge.pkl"]
print ("Internal: \n")
p=0
for name,model in models.items():
	model.fit(X_train, y_train)
	y_pred=model.predict(X_test)
	joblib.dump(model, loc[p])
	p+=1
	print(name)
	print("Coefficients: ", model.coef_)
	mse=mean_squared_error(y_test, y_pred)
	print("MSE: ", mse)
	r2=r2_score(y_test, y_pred)
	print("R2 Score: ", r2)
	print()
print("External: \n")
