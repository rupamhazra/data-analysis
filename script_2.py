from numpy import dtype
import pandas as pd

car = pd.read_excel("Cars Data1.xlsx",engine='openpyxl',) 
#print('data',car.head(2))
#print('car',car.shape)

'''
1) Instruction (For Data Cleaning)
	- Find all Null Value in the dataset. if there is any column, then fill it with the mean of that column

null_columns = car.columns[car.isna().any()].tolist() # Find all Null Value in the dataset
#print('null_columns',null_columns)

for each_column in null_columns:
	#print('column before',car[car[each_column].isna()])
	car[each_column].fillna(car[each_column].mean(),inplace=True)
	#print('column after',car[car[each_column].isna()])

#print('car',car)

'''

'''
2) Instruction (For Based on Value Counts)
	- Check what are the different types of Make are there in our dataset And what is the count(occurence) of each Make in the data ? 

print('type of make',car['Make'].value_counts())

'''

'''
3) Instruction (Filtering)
	- Show all the records where Origin is Asia or Europe

#print('car',car[(car['Origin']=='Asia') | (car['Origin'] == 'Europe')])

#print('car',car[car['Origin'].isin(['Asia','Europe'])])

'''
'''
4) Instruction (Removing unwanted records)
	- Remove all the records (rows) where Weight is above 4000

print('remove data',car.drop(car[car['Weight'] > 4000].index, inplace=True)) # Way 1
print('remove data',car[~(car['Weight'] > 4000)]) # Way 2
'''

'''
5) Instruction (Applying function on a column)
	- Increase all the values of 'MPG_City' column by 3.
'''
car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3)
print(car.head(5))



