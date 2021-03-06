# -*- coding: utf-8 -*-
"""Team_DivineAngle_Challenge1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p7f0v1GY79KJrF_eOBB3i5nzucTucz1y
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

from google.colab import drive
drive.mount('/content/drive')

Formula_pd=pd.read_csv('/content/drive/MyDrive/WeatherDataSet/weather.csv',low_memory=False)

Formula_pd['M_SAFETY_CAR_STATUS'].unique()

Formula_pd.shape

# Formula_pd['TIMESTAMP']=pd.to_datetime(Formula_pd['TIMESTAMP'],unit='s')

Formula_pd.describe()

Formula_pd=Formula_pd[Formula_pd.M_NUM_WEATHER_FORECAST_SAMPLES!=0]

Formula_pd.shape

Formula_pd=Formula_pd[Formula_pd.M_SESSION_UID!=0]

Formula_pd.shape

Formula_pd.columns

Formula_pd['M_SAFETY_CAR_STATUS'].unique()

Formula_pd.isnull().sum()

Formula_pd['M_TIME_OFFSET'].unique()

len(Formula_pd['M_SESSION_TIME'].unique())

F1=Formula_pd.drop(columns=['Unnamed: 58'],axis=1,inplace=False)

F1.isnull().sum()

Formula_pd['TIMESTAMP'].unique()

F1.dtypes

F1.shape

F1=F1.iloc[:,7:]
F1.head()

F1.shape

F1.columns

F1.drop(columns=['M_PIT_RELEASE_ASSIST','M_GEARBOX_ASSIST','M_GAME_PAUSED','GAMEHOST','M_SLI_PRO_NATIVE_SUPPORT','M_SAFETY_CAR_STATUS','M_FORMULA','M_PIT_ASSIST','M_SPECTATOR_CAR_INDEX','M_DYNAMIC_RACING_LINE_TYPE','M_AI_DIFFICULTY','M_NETWORK_GAME','M_STEERING_ASSIST','M_IS_SPECTATING'],inplace=True)

F1.shape

F1.columns

F1.drop(columns=['M_FRAME_IDENTIFIER','M_PLAYER_CAR_INDEX','M_SECONDARY_PLAYER_CAR_INDEX', 'M_BRAKING_ASSIST','M_SESSION_LINK_IDENTIFIER', 'M_ZONE_START', 'M_ZONE_FLAG',
       'M_PIT_STOP_WINDOW_IDEAL_LAP'],inplace=True)

F1.columns

F1.drop(columns=['M_ERSASSIST','M_SESSION_TYPE','M_PIT_STOP_WINDOW_LATEST_LAP', 'M_WEEKEND_LINK_IDENTIFIER',
       'M_SESSION_TIME_LEFT','M_SESSION_DURATION',
       'M_PIT_STOP_REJOIN_POSITION','M_PIT_SPEED_LIMIT', 'M_TOTAL_LAPS', 'M_DYNAMIC_RACING_LINE',
       'M_DRSASSIST'],inplace=True)

F1.columns

F1.isnull().sum()

F1.shape

F1.dropna(inplace=True)

F1.shape

Y=F1['M_RAIN_PERCENTAGE']
X=F1.drop(columns=['M_RAIN_PERCENTAGE'],inplace=False)

Formula_pd[Formula_pd.M_TIME_OFFSET==5]['TIMESTAMP'].iloc[:10]
# Formula_pd.columns

Y.head()

X.head()

Y.isnull().sum()

X.columns

X.drop(columns=['M_NUM_MARSHAL_ZONES'],inplace=True)
X.drop(columns=['M_TRACK_LENGTH','M_TRACK_TEMPERATURE_CHANGE'],inplace=True)
X.head()
X.drop(columns=['M_WEATHER_FORECAST_SAMPLES_M_WEATHER','M_WEATHER_FORECAST_SAMPLES_M_TRACK_TEMPERATURE','M_WEATHER_FORECAST_SAMPLES_M_AIR_TEMPERATURE','M_NUM_WEATHER_FORECAST_SAMPLES'],inplace=True)
X['M_SEASON_LINK_IDENTIFIER'].unique()
X.drop(columns=['M_SEASON_LINK_IDENTIFIER'],inplace=True)

X.columns

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, Y,random_state = 0)

X.head()

forest_model = RandomForestRegressor(random_state=100)
forest_model.fit(train_X, train_y)
pred = forest_model.predict(val_X)
print(mean_absolute_error(val_y,pred))

from sklearn import metrics
forest_model.score(val_X,val_y)

Y111=val_y.values

Y111[:100]

pred[:100]

Y.mode()

X.columns

y_val1=forest_model.predict(val_X.iloc[0:100])
for i in range(len(y_val1)):
    print(y_val1[i],"predicted value",val_y.iloc[i],"is the actual value")

from xgboost import XGBRegressor

my_model = XGBRegressor()
my_model.fit(train_X,train_y)

my_model.score(val_X,val_y)

y_val2=my_model.predict(val_X.iloc[0:100])
for i in range(len(y_val1)):
    print(y_val2[i],"predicted value",val_y.iloc[i],"is the actual value")

y_c=F1['M_WEATHER']
x_c=F1.drop(columns=['M_WEATHER'],inplace=False)

from sklearn.model_selection import train_test_split as tts
x_ctrain,x_ctest,y_ctrain,y_ctest = tts(x_c,y_c,test_size=0.25,random_state=0)

#Decision Tree Classifier for max depth=2

from sklearn import tree
clf = tree.DecisionTreeClassifier(max_depth = 2).fit(x_ctrain,y_ctrain)
clf.predict(x_ctest)
tree.plot_tree(clf)

print(clf.predict(x_ctest))
clf.score(x_ctest,y_ctest)

#DecisionTree Classifier with maxdepth = 3

clf1 = tree.DecisionTreeClassifier(max_depth = 3).fit(x_ctrain,y_ctrain)
clf1.predict(x_ctest)
tree.plot_tree(clf1)

print(clf1.predict(x_ctest))
clf1.score(x_ctest,y_ctest)

#Decision Tree Classifier for max depth=5

from sklearn import tree
clf2 = tree.DecisionTreeClassifier(max_depth = 5).fit(x_ctrain,y_ctrain)
clf2.predict(x_ctest)
tree.plot_tree(clf2)

print(clf2.predict(x_ctest))
clf2.score(x_ctest,y_ctest)

print(set(clf2.predict(x_ctest)))

#Decision Tree Classifier for max depth=8

from sklearn import tree
clf3 = tree.DecisionTreeClassifier(max_depth = 8).fit(x_ctrain,y_ctrain)
clf3.predict(x_ctest)
tree.plot_tree(clf3)

clf3.score(x_ctest,y_ctest)

from sklearn import tree
clf4 = tree.DecisionTreeClassifier(max_depth = 8,criterion="entropy").fit(x_ctrain,y_ctrain)
clf4.predict(x_ctest)
tree.plot_tree(clf3)

clf4.score(x_ctest,y_ctest)