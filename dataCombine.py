import pandas as pd
import numpy as np
import os

import loadData as ld
dir_path = ld.dir_path

train = ld.load('train.csv')

userFeatures = ld.load('user.csv')

data = pd.merge(train.head, userFeatures, on=['userID'], how='left')

print data.head(10)																											

#data.to_csv(r'data.csv', encoding='gbk')
