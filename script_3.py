import pandas as pd

police_data = pd.read_excel('Police Data.xlsx',engine='openpyxl')
#print(police_data.head(2))

'''
Data Cleaning
	- Remove the column that only contains missing values

#print(police_data.columns[police_data.isna().any()])

#null_columns = police_data.columns[police_data.isna().any()].tolist()
#print('null_columns',null_columns)
#print(police_data.drop(columns=null_columns))
#print(police_data.head(2))
'''

'''
	Question (Based on Filtering + Value Counts)
	- For Speeding, were Men or Women stopped more often? 

print(police_data[police_data['violation']=='Speeding'].driver_gender.value_counts())
'''

'''
	Does gender affect who gets searched during a stop

print(police_data.groupby('driver_gender').search_conducted.sum())
'''
'''
find the mean of stop ducration

#print(police_data.stop_duration.value_counts())

# convert the value from string to int for getting mean value

police_data['stop_duration'] = police_data['stop_duration'].map({'0-15 Min':7.5,'16-30 Min':24, '30+ Min':45})
print(police_data.head(2))

'''

'''
Compare the age distributions for each violation
'''
print(police_data.groupby('violation').driver_age.describe())


