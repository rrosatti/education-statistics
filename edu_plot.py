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

	ax1.set_xticks(x)
	ax1.set_xticklabels(x, rotation=50)

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
	ys = [np.array(df.iloc[i]) for i in range(0, 8)]
	ylabels = ['Post-secondary non-tertiary', 'Pre-primary', 'Primary and lower secondary (excluding repetition)', 
				'Primary and lower secondary', 'Primary and secondary', 'Primary to tertiary', 'Secondary', 'Tertiary']

	for i, y in enumerate(ys):
		ax1.plot(x, y, label=ylabels[i], color=np.random.rand(3,1))

	ax1.set_xticks(x)
	ax1.set_xticklabels(x, rotation=50)

	fontP = FontProperties()
	fontP.set_size('small')

	plt.xlabel('Years')
	plt.ylabel('School Life Expectancy (Years)')
	plt.title('School Life Expectancy ({})'.format(op), fontsize=15)
	plt.legend(loc=0, prop=fontP)
	plt.subplots_adjust(bottom=0.15)
	plt.show()

def plot_enrolment_analysis(df):
	print(df)
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))

	x = list(df.columns)
	ys = [np.array(df.iloc[i]) for i in range(0, 8)]
	ylabels = ['Early childhood', 'Lower secondary', 'Post-secondary non-tertiary', 'Pre-primary', 'Primary',
				'Secondary', 'Tertiary', 'Upper Secondary']

	for i, y in enumerate(ys):
		ax1.plot(x, y, label=ylabels[i], color=np.random.rand(3,1))

	ax1.set_xticks(x)
	ax1.set_xticklabels(x, rotation=50)

	plt.xlabel('Years')
	plt.ylabel('Enrolment (%)')
	plt.title('Percentage of enrolment')
	plt.legend(loc=0)
	plt.subplots_adjust(bottom=0.15)
	plt.show()

def plot_expenditure_analysis(df):
	print(df)
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))

	x = list(df.columns)
	ys = [np.array(df.iloc[i]) for i in range(0,9)]
	ylabels = ['Expenditure on education as (%) of total government expenditure on education', 'Early childhood', 'Lower secondary', 
				'Post-Secondary non-tertiary', 'Pre-primary', 'Primary',
				'Secondary', 'Tertiary', 'Upper secondary']

	for i, y in enumerate(ys):
		ax1.plot(x, ys[i], label=ylabels[i], color=np.random.rand(3,1))

	ax1.set_xticks(x)
	ax1.set_xticklabels(x, rotation=50)

	fontP = FontProperties()
	fontP.set_size('small')

	plt.xlabel('Years')
	plt.ylabel('Expenditure (%)')
	plt.title('Expenditure on education as percentage of governement expenditure on education (%)', fontsize=14)
	plt.legend(loc=9, prop=fontP, bbox_to_anchor=(0.5, -0.2))
	plt.subplots_adjust(bottom=0.35)
	plt.show()

def plot_student_population_analysis(df, op):
	print(df)
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))
	# this avoid the '1e7' notation in y axis
	plt.ticklabel_format(style='plain')

	x = list(df.columns)
	print(len(df))
	ys = [np.array(df.iloc[i]) for i in range(0, len(df))]
	ylabels = ['Ages 0-14', 'Ages 15-24']

	for i, y in enumerate(ys):
		ax1.plot(x, ys[i], label=ylabels[i], color=np.random.rand(3,1))

	ax1.set_xticks(x)
	ax1.set_xticklabels(x, rotation=50)

	plt.xlabel('Years')
	plt.ylabel('Student Population')
	plt.title('Mean Student Population ({})'.format(op), fontsize=16)
	plt.legend(loc=0)
	plt.subplots_adjust(bottom=0.15, left=0.1)
	plt.show()

def plot_student_population_analysis_all(df):
	print(df)
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))
	# this avoid the '1e7' notation in y axis (scientific notation?)
	plt.ticklabel_format(style='plain')

	x = list(df.columns)
	ys = [np.array(df.iloc[i]) for i in range(0, len(df))]
	ylabels = ['Ages 0-14 - Female', 'Ages 0-14 - Male', 'Ages 0-14 - Total', 
				'Ages 15-24 - Female', 'Ages 15-24 - Male', 'Ages 15-24 - Total']

	for i, y in enumerate(ys):
		ax1.plot(x, ys[i], label=ylabels[i], color=np.random.rand(3,1))

	ax1.set_xticks(x)
	ax1.set_xticklabels(x, rotation=50)

	fontP = FontProperties()
	fontP.set_size('small')

	plt.xlabel('Years')
	plt.ylabel('Student Population')
	plt.title('Mean Student Population', fontsize=16)
	plt.legend(loc=9, prop=fontP, bbox_to_anchor=(0.5, -0.2))
	plt.subplots_adjust(bottom=0.3, left=0.1)
	plt.show()

def plot_percentage_graduates_analysis(df, op):
	print(df)
	print(list(df.index))
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1),(0,0))

	x = list(df.columns)
	ys = [np.array(df.iloc[i]) for i in range(0, len(df))]
	ylabels = ['Agriculture', 'Education', 'Engineering, Manufacturing and Construction', 'Health and Welfare',
				'Humanities and Arts', 'Science', 'Social Sciences, Business and Law']
	
	for i,y in enumerate(ys):
		ax1.plot(x, y, label=ylabels[i], color=np.random.rand(3,1))

	ax1.set_xticks(x)
	ax1.set_xticklabels(x, rotation=50)

	fontP = FontProperties()
	fontP.set_size('small')

	plt.xlabel('Years')
	plt.ylabel('Percentage of Graduates (%)')
	plt.title('Percentage of Graduates  ({})'.format(op), fontsize=15)
	plt.legend(loc=0, prop=fontP, bbox_to_anchor=(0.6,-0.2))
	plt.subplots_adjust(bottom=0.35)
	plt.show()


