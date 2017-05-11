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
	reader = pd.read_csv(dir_path + '/pre/' + filename)
	return reader
	
def All():
	readers = {}
	j = 0
	for i in filenames:
		readers[i] = load(i)
		j += 1
	return readers
	
def User():
	return load('user.csv')
def UserAppInstal():
	return load('user_installedapps.csv')
def UserAppAction():
	return load('user_app_actions.csv')
def AppCat():
	return load('app_categories.csv')
def Ad():
	return load('ad.csv')
def Pos():
	return load('position.csv')


if __name__ == "__main__":
	#readall exceeds memory limit on my VM; could be
	#runnable on better settings
	readahs = All()

	for readah in readahs:
		print(readah.head(10).to_string())
