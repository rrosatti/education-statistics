import pandas as pd
import numpy as np
import pickle
from pathlib import Path

data_path = 'C:/Users/rodri/OneDrive/Documentos/python/data/education-statistics/'

def get_dataset():
	df = pd.read_csv(data_path+'data.csv')
	# this will select only the params: 'Country Name', 'Country Code', 'Inidicator Name', 'Indicator Code' 
	# and the years from 1977 to 2016
	df = df.iloc[:,:44]
	df.drop('Indicator Code', 1, inplace=True)
	save_pickle(df, 'selected_data.pickle')
	return df

def save_pickle(data, filename):
	with open(data_path+filename, 'wb') as f:
		pickle.dump(data, f)

def get_pickle(filename):
	with open(data_path+filename, 'rb') as f:
		data = pickle.load(f)
	return data

def file_exists(filename):
	if Path(data_path+filename).is_file():
		return True
	else:
		return False


