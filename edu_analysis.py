import edu_util as eutil
import pandas as pd
import numpy as np

filename = 'selected_data.pickle'
interesting_indicators = [
							'Adult literacy rate, population 15+ years, both sexes (%)',

							] 

def show_indicators(df):
	df2 = df.drop_duplicates(['Indicator Name'])
	indicators = df['Indicator Name'].tolist()
	print(indicators)


if eutil.file_exists(filename):
	df = eutil.get_pickle(filename)
else:
	df = eutil.get_dataset()

#print(df[ df['Indicator Name'] == 'Adult literacy rate, population 15+ years, both sexes (%)'])
eutil.get_indicators()