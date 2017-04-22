import pandas as pd
import numpy as np
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

filenames = ['user.csv',
'user_installedapps.csv',
'user_app_actions.csv',
'app_categories.csv',
'ad.csv',
'position.csv']

def load(filename):
	reader = pd.read_csv(filename)
	return reader
	
def loadAll():
	readers = {}
	j = 0
	for i in filenames:
		readers[i] = load(dir_path + '/pre/' + i)
		j += 1
	return readers
	
def loadUser():
	return load('user.csv')
def loadUserAppInstal():
	return load('user_installedapps.csv')
def loadUserAppAction():
	return load('user_app_actions.csv')
def loadAppCat():
	return load('app_categories.csv')
def loadAd():
	return load('ad.csv')
def loadPos():
	return load('position.csv')


if __name__ == "__main__":
	#readall exceeds memory limit on my VM; could be
	#runnable on better settings
	readahs = loadAll()

	for readah in readahs:
		print(readah.head(10).to_string())
