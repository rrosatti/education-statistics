import edu_util as eutil
import edu_plot as eplot
import pandas as pd
import numpy as np

filename = 'selected_data.pickle' 
data_path = 'C:/Users/rodri/OneDrive/Documentos/python/data/education-statistics/'

def show_indicators(df):
	df2 = df.drop_duplicates(['Indicator Name'])
	indicators = df['Indicator Name'].tolist()
	print(indicators)

def get_selected_indicators():
	df = pd.read_csv(data_path+'indicators_raw.txt', sep='\t')
	df = df[['Indicator Name']]
	df = df.sort_values(by='Indicator Name')
	indicators = df['Indicator Name'].tolist()
	return indicators

def apply_selected_indicators(df):
	indicators = get_selected_indicators()
	df2 = df[ df['Indicator Name'].isin(indicators)]
	return df2

def get_literacy_indicators():
	all_ind = get_selected_indicators()
	literacy_ind = []
	for ind in all_ind:
		if ('literacy' in ind):
			literacy_ind.append(ind)
	#print(literacy_ind)
	return literacy_ind

def get_school_life_expectancy_indicators():
	all_ind = get_selected_indicators()
	school_life_expct = []
	for ind in all_ind:
		if ('life expectancy' in ind):
			school_life_expct.append(ind)
	#print(life_expct)
	return school_life_expct

def get_enrolment_indicators():
	all_ind = get_selected_indicators()
	enrol_ind = []
	for ind in all_ind:
		if ('enrolment' in ind):
			enrol_ind.append(ind)
	#print(enrol_ind)
	return enrol_ind

def get_completion_rate_indicators():
	all_ind = get_selected_indicators()
	comp_rate = []
	for ind in all_ind:
		if ('completion' in ind):
			comp_rate.append(ind)
	#print(comp_rate)
	return comp_rate

def get_expenditure_indicators():
	all_ind = get_selected_indicators()
	expend_ind = []
	for ind in all_ind:
		if ('Expenditure' in ind):
			expend_ind.append(ind)
	#print(expend_ind)
	return expend_ind

def get_percentage_graduates_indicators():
	all_ind = get_selected_indicators()
	perct_grad_ind = []
	for ind in all_ind:
		if ('graduates' in ind):
			perct_grad_ind.append(ind)
	#print(perct_grad_ind)
	return perct_grad_ind

def get_student_population_indicators():
	all_ind = get_selected_indicators()
	student_pop_ind = []
	for ind in all_ind:
		if ('Population' in ind):
			student_pop_ind.append(ind)
	#print(student_pop_ind)
	return student_pop_ind

# op = {f: female, m: male, b: both}
def literacy_analysis(df, plot=False, op='b'):
	ops = {'f': 'female', 'm': ' male', 'b': 'both sexes'}
	indicators = get_literacy_indicators()
	# get only the indicators related with both sexes
	opInd = []
	for i in indicators:
		if (ops.get(op) in i):
			opInd.append(i)
	df2 = df[ df['Indicator Name'].isin(opInd) ]
	df2 = df2.groupby('Indicator Name').agg(['mean'])
	df2.columns = list(range(1977,2016))
	if plot:
		eplot.plot_literacy_analysis(df2, ops.get(op).lstrip())
	return df2

# op = {f: female, m: male, b: both}
def school_life_expectancy_analysis(df, plot=False, op='b'):
	ops = {'f': 'female', 'm': ' male', 'b': 'both sexes'}
	indicators = get_school_life_expectancy_indicators()
	opInd = []
	for i in indicators:
		if (ops.get(op) in i):
			opInd.append(i)
	df2 = df[ df['Indicator Name'].isin(opInd) ]
	df2 = df2.groupby('Indicator Name').agg(['mean'])
	df2.columns = list(range(1977,2016))
	if plot:
		eplot.plot_school_life_expectancy_analysis(df2, ops.get(op).lstrip())
	return df2
	

if eutil.file_exists(filename):
	df = eutil.get_pickle(filename)
else:
	df = eutil.get_dataset()

df = apply_selected_indicators(df)
#get_literacy_indicators()
#get_school_life_expectancy_indicators()
#get_enrolment_indicators()
#get_completion_rate_indicators()
#get_expenditure_indicators()
#get_percentage_graduates_indicators()
#get_student_population_indicators()

# analysing and ploting
#literacy_analysis(df, True, 'b')
school_life_expectancy_analysis(df, True, 'b')


