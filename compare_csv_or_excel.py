import imp
import openpyxl


import pandas as pd

df1 = pd.read_excel('file1.xlsx',engine='openpyxl')
df2 = pd.read_excel('file2.xlsx', engine='openpyxl')
print(df1.head(1))
print(df2.head(1))

# column names
print (pd.merge(df1, df2))

