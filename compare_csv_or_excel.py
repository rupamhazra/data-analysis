import imp
import openpyxl


import pandas as pd

df1 = pd.read_excel('file1.xlsx',engine='openpyxl')
df2 = pd.read_excel('file2.xlsx', engine='openpyxl')
print(df1.head(2))
print(df2.head(2))

# column names
print("=============================================")
#print (pd.merge(df1, df2))

df3 = pd.merge(df1, df2,how='left')

print(df3)

# Get the unmatched column name


# stored to third excel 
file_name = 'merge_file.xlsx'
df3.to_excel(file_name)

