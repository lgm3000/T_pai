import loadData as load
import pandas as pd
from sklearn import linear_model as lin
import numpy as np

traincsv = load.load('train100.csv')

reg = linear_model.LinearRegression()


