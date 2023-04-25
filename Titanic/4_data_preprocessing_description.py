# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 22:27:53 2022

@author: yijae
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

#read data from CSV file 
train = pd.read_csv('Titanic/train.csv')
test = pd.read_csv('Titanic/test_titanic.csv')



train_data_error = train.isnull().sum()
print(train_data_error)

test_data_error = test.isnull().sum()
print(test_data_error)

#data cleaning if there is none of age
replace = train['Age'].mean()
train['Age'] = train['Age'].fillna(replace)
test['Age'] = test['Age'].fillna(replace)

#female data만 골라 data set을 구성하시오
train['IsFemale'] = (train['Sex'] == 'female')
test['IsFemale'] = (test['Sex'] == 'female') 

#dimension vector 
predictors = ['Pclass', 'IsFemale', 'Age']

x_test = pd.DataFrame(test, columns= predictors)
y_test = test["Survived"]
#make train and test set for validation
x_train = pd.DataFrame(train, columns=predictors)
y_train = train["Survived"]

#x_test
#y_true
#make label Survied status
model = LogisticRegression()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)
print(y_predict[:])

print((y_test == y_predict).mean())