'''
Pokud jsi v minulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.

- Vyfiltruj si informace o teplotách 13. listopadu 2017.
- Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
- Vypočti počet dat, které máš pro daný den za jednotlivé regiony.
- Vypočti průměrnou teplotu za jednotlivé regiony.
- Vypočti maximální a minimální teplotu v každém regionu.
'''

import pandas as pd
import pytemperature


import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

teploty = pd.read_csv('temperature.csv')
print(teploty.head())

# prevod na stupně Ceslia (f2c)
teploty['AVG_ve_stupnich_Celsia'] = pytemperature.f2c(teploty['AvgTemperature'])
print(teploty.head())

# teploty 13.11.2017
print(teploty[teploty['Day'] == 13])

# vyřadit teploty -99 (podmíněné sloupce)
# kolik jich vlastně je??  ( = 49 )
print(teploty[teploty['AvgTemperature'] == -99].count())

#knihovna numpy
import numpy as np
teploty['chybne'] = np.where(teploty['AvgTemperature'] == -99, None, 'ok')
print(teploty[teploty['chybne'].isnull()])
#smazání všech None hodnot
teploty = teploty.dropna();
#kontrola
print(teploty[teploty['chybne'].isnull()])

#počet dat, pro daný region a den
print(teploty.groupby('Region')['Day'].count())

# průměrná teplota ve °C v regionech
print(round(teploty.groupby('Region')['AVG_ve_stupnich_Celsia'].mean(),1))

# max a min teplota ve °C v každém regionu
print(round(teploty.groupby('Region')['AVG_ve_stupnich_Celsia'].max(),1))
print(round(teploty.groupby('Region')['AVG_ve_stupnich_Celsia'].min(),1))

