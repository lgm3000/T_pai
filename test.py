#!/usr/bin/env python
import math
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from numpy import loadtxt, where

df = pd.read_csv("data.csv")
df.columns = ["grade1", "grade2", "label"]

X = df[["grade1", "grade2"]]
X = np.array(X)
Y = df["label"].map(lambda x: float(x.rstrip(';')))
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, Y_train)
result = clf.predict(X_test)
print classification_report(Y_test, result)
print 'score Scikit learn: ', clf.score(X_test,Y_test)

pre = clf.predict_proba(Y)
output = pd.DataFrame(pre)
output.index = Y.index
output.columns= ['0', 'probability']
output.drop('0',axis = 1, inplace = True)
print output.head(5)

output.to_csv('output.csv')
