'''Pokračuj ve své práci s informacemi o průměrných teplotách. Pokud jsi zpracovala pokročilou variantu 24,
můžeš pracovat s teplotami ve stupních Celsia.
Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky. Dále napiš následující dotazy:
- Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
- Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country
hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
- Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia.'''

import pandas as pd
import pytemperature
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

teplota = pd.read_csv('temperature.csv')

teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])
print(teplota[teplota['City'] == 'Prague'][['City', 'AvgTemperatureCelsia']])

print(teplota.head())

# 13.11.2017
print(teplota[teplota['Day'] == 13][['Day', 'City', 'AvgTemperatureCelsia']])
# US
novaTabulka = teplota[(teplota['Day'] == 13) & (teplota['Country'] == 'US')]
print(novaTabulka)
# Washington a Philadelphia
print(novaTabulka[(novaTabulka['City'] == 'Washington') | (novaTabulka['City'] == 'Philadelphia')][['City', 'AvgTemperatureCelsia']])

# dobrovolný úkol: průměrná hodnoty dne 13.11.2017 v USA
prumer = novaTabulka['AvgTemperatureCelsia'].mean()
print(f"Průměrná hodnota naměřených teplot dne 13.11.2017 v US byla: {round(prumer,2)} stupňů Celsia.")

# statistika: medián a roztyl pro Celsiovy teploty
median = novaTabulka['AvgTemperatureCelsia'].median()
rozptyl = novaTabulka['AvgTemperatureCelsia'].var()
print(f"Medián: {median}")
print(f"Rozptyl: {rozptyl}")