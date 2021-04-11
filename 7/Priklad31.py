'''Pokud jsi v předminulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve
stupních Celsia:
- Vyfiltruj si informace o teplotách 13. listopadu 2017.
- Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
- Seřad hodnoty v souboru podle teploty od největší po nejmenší.
- Vypiš pět měst s nejvyšší teplotou a pět měst s nejnižší teplotou.
'''

import wget
import pandas as pd
import pytemperature
import matplotlib.pyplot as plt

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

teploty = pd.read_csv('temperature.csv')
print(teploty.head())

# prevod na stupně Ceslia (f2c)
teploty['AVG_ve_stupnich_Celsia'] = pytemperature.f2c(teploty['AvgTemperature'])
print(teploty.head())

# teploty 13.11.2017
print(teploty[teploty['Day'] == 13])

# vyřazení všech teplot = -99
import numpy as np
teploty['chybne'] = np.where(teploty['AvgTemperature'] == -99, None, 'ok')
teploty = teploty.dropna()

# seřazení hodnot od nejvyšší po nejnižší
teploty = teploty.sort_values(by='AVG_ve_stupnich_Celsia', ascending=False)

# vypsání prvních/posledních měst s nejvyšší/nejnižší (+ který den v listopadu to bylo...)
print(teploty[['City','Day','AVG_ve_stupnich_Celsia']].head())
print(teploty[['City','Day','AVG_ve_stupnich_Celsia']].tail())

# vykreslím si průměrné teploty v Regionech
teploty = teploty.groupby('Region')['AVG_ve_stupnich_Celsia'].mean().plot(kind='bar', color='orange')
plt.show()

