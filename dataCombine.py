import pandas as pd
import numpy as np
import os

import loadData as ld
dir_path = ld.dir_path

train = ld.load('train.csv')

usr = ld.load('user.csv')
pos = ld.load('position.csv')

train = pd.merge(train.head(100), usr, on=['userID'], how='left')
train = pd.merge(train, pos, on=['positionID'], how='left')

del train['userID']
del train['positionID']

print train.head(10)																											
dira = dir_path + '/data.csv'
print(dira)
train.to_csv(dira, encoding='gbk')
