# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 22:53:49 2021

@author: doguilmak

dataset: https://archive.ics.uci.edu/ml/datasets/Solar+Flare

-Predict C-class, M-class and X-class in one algorithm.
-Predict flare size.

"""
#%%
# 1. Importing Libraries

from sklearn.impute import SimpleImputer
import seaborn as sns
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Activation
import time
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#%%
# 2. Data Preprocessing

# 2.1. Uploading data
start = time.time()
data = pd.read_csv('flare.data1', sep=" ", skiprows=1, header=None)

# 2.2. Looking For Anomalies
print(data.head())
print(data.info())
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
X = newData[:, 0:10]

for i in range(10, 13):
    y = newData[:, i]
    if i == 10:
        print('\n\n----- C-class Flares Prediction -----\n\n')
    elif i == 11:
        print('\n\n----- M-class Flares Prediction -----\n\n')
    else:
        print('\n\n----- X-class Flares Prediction -----\n\n')

#%%
# 3 Artificial Neural Network
    
    # 3.1. Creating layers
    model = Sequential()
    model.add(Dense(64, input_dim=10))
    model.add(Activation('relu'))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('softmax'))
    
    # 3.2. Compile and fit the data
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model_history = model.fit(X, y, epochs=64, batch_size=32, validation_split=0.13)
    
    # 3.5. Plot accuracy and val_accuracy
    print(model_history.history.keys())
    plt.figure(figsize=(10, 10))
    sns.set_style('whitegrid')
    plt.plot(model_history.history['accuracy'])
    plt.plot(model_history.history['val_accuracy'])
    if i == 10:
         plt.title('C-class Flares Model Accuracy')
    elif i == 11:
         plt.title('M-class Flares Model Accuracy')
    else:
         plt.title('X-class Flares Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.ylim(0, 1.01)
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    
    import statistics
    mean_val_accuracy = statistics.mean(model_history.history['val_accuracy'])
    print(f'\nMean of validation accuracy: {mean_val_accuracy}')    
    
    # Predicting class
    predict_model = X[0:1,]
    print(f'Model predicted class as {model.predict_classes(predict_model)}.')
        
#%%
# XGBoost
    
    # 3.4. Splitting test and train 
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
    
    # 3.5. Scaling datas
    from sklearn.preprocessing import StandardScaler
    sc=StandardScaler()
    
    X_train = sc.fit_transform(x_train) 
    X_test = sc.transform(x_test) 
    
    from xgboost import XGBClassifier
    classifier= XGBClassifier()
    classifier.fit(X_train, y_train)
    
    y_pred = classifier.predict(X_test)
    
    # 3.6. Prediction
    print('\nXGBoost Prediction')
    predict_model_XGBoost = X[0:1,]
    print(f'Model predicted class as {classifier.predict(predict_model_XGBoost)}.')    
    
    # 3.7. Confusion matrix and accuracy score
    from sklearn.metrics import confusion_matrix
    cm2 = confusion_matrix(y_pred, y_test)  # Comparing results
    print("\nConfusion Matrix(XGBoost):\n", cm2)
    
    from sklearn.metrics import accuracy_score
    print(f"\nAccuracy score(XGBoost): {accuracy_score(y_test, y_pred)}")


end = time.time()
cal_time = end - start
print("\nProcess took {} seconds.".format(cal_time))
