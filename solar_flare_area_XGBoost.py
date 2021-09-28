# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 22:08:08 2021

@author: doguilmak

dataset: https://archive.ics.uci.edu/ml/datasets/Solar+Flare

Predict area with XGBoost.

"""
#%%
# 1. Importing Libraries

from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")

#%%
# 2. Data Preprocessing

# 2.1. Importing Data
start = time.time()
data = pd.read_csv('flare.data2', sep=" ", skiprows = 1,header = None)

# 2.2. Looking For Anomalies
print(data.info())
print(data.head())
print("\n", data.head())
print("\n", data.describe().T)

# 2.4. Label Encoding Proccess
from sklearn.preprocessing import LabelEncoder
data = data.apply(LabelEncoder().fit_transform)
print("data:\n", data)
data.replace('?', -999999, inplace=True)

imputer = SimpleImputer(missing_values= -999999, strategy='mean')
newData = imputer.fit_transform(data)

# 2.5. Determination of Dependent and Independent Variables

x1 = newData[:, 0:8]
x2 = newData[:, 9:14]

X = np.concatenate((x1, x2), axis=1)
y = newData[:, 8:9]

# 2.6. Splitting Test and Train 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

# 2.7. Scaling Datas
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

X_train = sc.fit_transform(x_train) 
X_test = sc.transform(x_test) 

#%%
# 3 XGBoost

from xgboost import XGBClassifier
classifier= XGBClassifier()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# 3.6. Prediction
print('\nXGBoost Prediction')
predict_model_XGBoost = X[0:1,]
if classifier.predict(predict_model_XGBoost) == 0:
    print('Model predicted as small.')
    print(f'Model predicted class as {classifier.predict(predict_model_XGBoost)}.')
else:
    print('Model predicted as large.')    
    print(f'Model predicted class as {classifier.predict(predict_model_XGBoost)}.')

# Creating Confusion Matrix
from sklearn.metrics import confusion_matrix
cm2 = confusion_matrix(y_pred, y_test)  # Comparing results
print("\nConfusion Matrix(XGBoost):\n", cm2)

# Accuracy of XGBoost
from sklearn.metrics import accuracy_score
print(f"\nAccuracy score(XGBoost): {accuracy_score(y_test, y_pred)}")

end = time.time()
cal_time = end - start
print("\nProcess took {} seconds.".format(cal_time))
