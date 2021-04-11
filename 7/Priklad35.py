'''
Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
- Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
- Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých
městech v listopadu 2017.
'''

import wget
import pandas as pd
import pytemperature
import matplotlib.pyplot as plt
import numpy

teploty = pd.read_csv('temperature.csv')
#print(teploty.head())

teploty['AVG_ve_stupnich_Celsia'] = pytemperature.f2c(teploty['AvgTemperature'])
print(teploty.head())

helsinki = teploty[teploty['City'] == 'Helsinki']
helsinki = helsinki['AVG_ve_stupnich_Celsia']
#print(helsinki.head())
tokyo = teploty[teploty['City'] == 'Tokyo']
tokyo = tokyo['AVG_ve_stupnich_Celsia']
#print(tokyo.head())
miami = teploty[teploty['City'] == 'Miami Beach']
miami = miami['AVG_ve_stupnich_Celsia']
#print(miami.head())

# převod na list teplot
helsinki_List = helsinki.to_numpy().tolist()
tokyo_List = tokyo.to_numpy().tolist()
miami_List = miami.to_numpy().tolist()

# pro kontrolu
#print(helsinki_List)
#print(tokyo_List)
#print(miami_List)

#spojení seznamů do DF
teplotyDF = pd.DataFrame(list(zip(helsinki_List, tokyo_List, miami_List)), columns=['Helsinki', 'Tokyo', 'Miami Beach'])
print(teplotyDF.head(n=10))

teplotyDF.plot(kind='box', grid=True)
plt.show()

