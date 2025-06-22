#visuals module of EXIF Predictor package of LensIQ Suite



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def compare_ev(test, pred):
	plt.scatter(test, pred, color='dodgerblue', edgecolor='k', alpha=0.7)
	plt.xlabel("Actual EV")
	plt.ylabel("Predicted EV")
	plt.title("Actual vs Predicted EV")
	plt.grid(True)
	plt.show()

def residualplot(test, pred):
	residuals=test-pred
	plt.figure(figsize=(8,6))
	plt.scatter(pred, residuals, color='dodgerblue', edgecolor='k', alpha=0.6)
	plt.axhline(0, color='red', linestyle='--', linewidth=2)
	plt.xlabel("Predicted EV")
	plt.ylabel("Residuals")
	plt.title("Residual Plot")
	plt.grid(True)
	plt.show()

def ev_time(df):
	df['Time'] = df['hour'] + df['min'] / 60
	plt.scatter(df['Time'], df['Predicted EV'], alpha=0.5)
	plt.xlabel("Hour")
	plt.ylabel("EV")
	plt.title("Predicted EV vs Time of Day")
	plt.grid(True)
	plt.show()

def ev_features(df):
	sns.pairplot(df[['Predicted EV', 'Aperture', 'log_ss', 'log_iso']])
	plt.title("Predicted EV vs rest")
	plt.grid(True)
	plt.show()
