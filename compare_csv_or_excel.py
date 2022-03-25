import imp
import openpyxl


import pandas as pd

df1 = pd.read_excel('file1.xlsx',engine='openpyxl')
df2 = pd.read_excel('file2.xlsx', engine='openpyxl')
#print(df1.head(1))
#print(df2.head(1))

# Drop duplicates
# df1 = df1['Rep'].drop_duplicates()
# print(df1)

# column names
#print (pd.merge(df1, df2))

'''
    Compare CSV/Excel Find Unmatched Rows 
'''

#a = df1[df1.eq(df2).all(axis=1) == False]

#print(a)
#print("======================")

#result = df1[~df1.apply(tuple, 1).isin(df2.apply(tuple,1))]

#print(result)

result = df1.merge(df2,left_on=df1.columns.tolist(),right_on=df2.columns.tolist())

df1.rename(columns= lambda x:x+'_file1',inplace=True)
#print(df1)

df2.rename(columns= lambda x:x+'_file2',inplace=True)
print(result)

