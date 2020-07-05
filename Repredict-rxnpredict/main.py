import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from sklearn.metrics import mean_squared_error,r2_score
def extract(datadir):
    inputs=pd.read_csv(datadir,index_col=0)
    yields=inputs['yields']
    train=inputs.drop(['yields','additive','halide','base','ligand'],axis=1)
    scaler=StandardScaler()
    scaler.fit(train)
    train=scaler.transform(train)
    return [train,yields]
X_data=extract('train.csv')[0]
Y_data=extract('test.csv')[0]
X_yield=extract('train.csv')[1]
Y_yield=extract('test.csv')[1]
model=RandomForestRegressor(n_estimators=500,random_state=42)
model.fit(X_data,X_yield)
preds=model.predict(Y_data)
r_squared=r2_score(preds,Y_yield)
rmse=mean_squared_error(preds,Y_yield)**0.5
plt.figure(figsize=(5,5))
r2_patch = mpatches.Patch(label="R2={:04.2f}".format(r_squared))
rmse_patch = mpatches.Patch(label="RMSE={:04.2f}".format(rmse))
plt.xlim(-25,105)
plt.ylim(0,105)
plt.scatter(preds, Y_yield, alpha=0.2)
plt.legend(handles=[r2_patch, rmse_patch])
#plt.show()
plt.savefig('predict_four_dimensions.jpg')

