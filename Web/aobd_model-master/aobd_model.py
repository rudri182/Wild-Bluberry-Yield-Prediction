
import numpy as np
import sys
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error 
from xgboost import plot_importance
from matplotlib import pyplot

data = pd.read_csv("WildBlueberry.csv")
data = data.drop(['Row#'], axis=1)
X = data.drop('yield',axis=1)
Y = data['yield']
SS = StandardScaler()
X = SS.fit_transform(X)
X = data[["honeybee","andrena","osmia","MaxOfUpperTRange","RainingDays","fruitset","seeds"]]
Y = data["yield"]
  
X_train_xg, X_test_xg, y_train_xg, y_test_xg = train_test_split(X, Y, test_size=0.2, random_state=0)
xg_reg = xgb.XGBRegressor(objective ='reg:linear')
xg_reg.fit(X_train_xg,y_train_xg)

preds_xg = xg_reg.predict(X_test_xg)

print('Train Score: ', xg_reg.score(X_train_xg, y_train_xg))  
print('Test Score: ', xg_reg.score(X_test_xg, y_test_xg)) \

# #MAE
print(metrics.mean_absolute_error(y_test_xg,preds_xg))
# #RMSE
print(np.sqrt(metrics.mean_squared_error(y_test_xg,preds_xg)))