from numpy import dtype
import pandas as pd

data = pd.read_excel("Weather_Data.xlsx",engine='openpyxl',) 

# Analyze data frames	
#print('data',data.head(5))

# it shows the shape
#print('shape',data.shape)

# it shows the all columns
#print('data',data.columns)

# it shows the data types of each column
#print('data',data.dtypes)

# it shows the data type of specific column
#print('data',data['Press_kPa'].dtype)

# it shows total number of unique values of specific column
#print('data',data['Date/Time'].unique())

# it shows total number of unique values on each column
#print('data',data.nunique())

# it shows the total no of non-null values in each column
#print('data',data.count())

# in a column, it shows all the unique values with their count
#print('data',data['Weather'].value_counts()) 

# it shows the all the info of data frame
#print('data',data.info())

# Find all the unique 'Wind	Speed' values in the data
#print('data',data['Wind Speed_km/h'].unique())	

'''
 	Find the number of times when the 'Weather is exactly Clear'.
'''
# print('data',data['Weather'].value_counts())

# Filtering data
#print('data',data[data.Weather=='Clear'])

# Group by
#print('data',len(data.groupby('Weather').get_group('Clear')))

'''
	Find the number of times when the "Wind speed was exactly 4km/h".
'''
#print('data',data.head(2))

# print('data',data.groupby('Wind Speed_km/h').get_group(4))
#print('data', data[data['Wind Speed_km/h'] == 4])

'''
	Find out all the Null Values in the data
'''
 
#print('data',data.isnull().sum())

# null values of Specific column
#print('data',data['Wind Speed_km/h'].isnull().sum())

'''
	Find out all the NotNull Values in the data
'''
#print('data',data.notnull().sum())

'''
	Rename the column name 'Weather' of the dataframe to 'Weather Condition'
'''
#print('data',data.rename(columns={'Weather':'Weather Condition'},inplace=True))
#print('data',data.head(1))

'''
	What is the mean 'Visibility'?
'''
#print('data',data.head(2))

#print('data',data['Visibility_km'].mean())

'''
	What is standard deviation of 'Pressure' in this data?
'''
#print('data',data['Press_kPa'].std())

'''
	What is the Variance of 'Relative Humidity' in this data
'''
#print('data',data.head(2))

#print('data',data['Rel Hum_%'].var())

'''
	Find all instances when 'Snow' was recorded
'''
#print('data',data[data['Weather'].str.contains('Snow')])

'''
	Find all instances when "Wind speed is above 24" and "Visibility is 25"
'''
#print('data',data[(data['Wind Speed_km/h']>24) & (data['Visibility_km'] == 25)])

'''
	What is the Mean value of each column against each 'Weather Condition'?
'''
#print('data',data.groupby('Weather').mean())

'''
	What is the minimum and maximum value of each column against each 'Weather Condition'
'''
#print('data',data.groupby('Weather').max())

