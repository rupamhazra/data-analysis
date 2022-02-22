# import pandas as pd

# covid_data = pd.read_excel("covid_19_data.xlsx",engine='openpyxl',)

# print(covid_data.head(2))

# # In which region, maximum number of Confirmed cases were recorded?
# result  = covid_data.groupby('Region').Confirmed.sum().sort_values(ascending=False)
# #print('result',result.idxmax())

# # How Many Confirmed, Deaths, & Recovered cases were reported from india till 29th april 2020?
# print(covid_data(covid_data['Date'] < '2020-04-29'))
