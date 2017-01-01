import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.font_manager import FontProperties
import numpy as np
import random

style.use('fivethirtyeight')

# op might be 'female', 'male' or 'both sexes'
def plot_literacy_analysis(df, op):
	print(df)
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))

	x = list(df.columns)
	y1 = np.array(df.iloc[0]) # Adult
	y2 = np.array(df.iloc[1]) # Elderly 
	y3 = np.array(df.iloc[2]) # Youth

	ax1.plot(x, y1, label='Adult', color='darkgoldenrod')
	ax1.plot(x, y2, label='Elderly', color='darkred')
	ax1.plot(x, y3, label='Youth', color='darkcyan')

	ax1.set_xticklabels(x, rotation=45)

	plt.xlabel('Years')
	plt.ylabel('Literay Rate Percentage')
	plt.title('World Literacy Rate from {} to {} ({}).'.format(str(x[0]), str(x[-1]), op), fontsize=16)
	plt.legend(loc=0)
	plt.subplots_adjust(bottom=0.15)
	plt.show()

def plot_school_life_expectancy_analysis(df, op):
	print(df, op)
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))

	x = list(df.columns)
	y1 = np.array(df.iloc[0]) # post-secondary non-tertiary
	y2 = np.array(df.iloc[1]) # pre-primary
	y3 = np.array(df.iloc[2]) # primary and lower secondary (excluding repetition)
	y4 = np.array(df.iloc[3]) # primary and lower secondary
	y5 = np.array(df.iloc[4]) # primary and secondary
	y6 = np.array(df.iloc[5]) # primary to tertiary
	y7 = np.array(df.iloc[6]) # secondary
	y8 = np.array(df.iloc[7]) # tertiary
	ys = [np.array(df.iloc[i]) for i in range(0, 8)]
	ylabels = ['Post-secondary non-tertiary', 'Pre-primary', 'Primary and lower secondary (excluding repetition)', 
				'Primary and lower secondary', 'Primary and secondary', 'Primary to tertiary', 'Secondary', 'Tertiary']

	for i, y in enumerate(ys):
		ax1.plot(x, y, label=ylabels[i], color=np.random.rand(3,1))

	ax1.set_xticklabels(x, rotation=45)

	fontP = FontProperties()
	fontP.set_size('small')

	plt.xlabel('Years')
	plt.ylabel('School Life Expectancy (Years)')
	plt.title('School Life Expectancy ({})'.format(op), fontsize=15)
	plt.legend(loc=0, prop=fontP)
	plt.show()
