'''Stáhni si soubor temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
- Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.
- Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být?
Zde je nápověda (nutno přepočítat...)
- Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
- Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region)
 Evropa (Europe).
- Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.
- Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
- Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu
(sloupec Region) Evropa (Europe).
- Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů.
Jsou některé hodnoty podezřelé?
'''

import pandas as pd
import pytemperature
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

teplota = pd.read_csv('temperature.csv')

teplota.info()
print(teplota.head(n=40))

# Praha
print(teplota[teplota['City'] == 'Prague']['AvgTemperature'])

# teplota vyšší než 80
print(teplota[teplota['AvgTemperature'] >= 80][['City','AvgTemperature']])

# teplota vyšší než 60, který den to bylo v Evropě, ...
print(teplota[(teplota['AvgTemperature'] >= 60) & (teplota['Region'] == 'Europe')][['City','Day','AvgTemperature']])

# extrémní teploty >80 a <-20
print(teplota[(teplota['AvgTemperature'] >= 80) | (teplota['AvgTemperature'] <= -20) ][['City','AvgTemperature']])
print(teplota[teplota['AvgTemperature'] <= -20][['City','AvgTemperature']])

# přidání dalšího sloupce do tab. a přepočet f2c
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])
print(teplota[teplota['City'] == 'Prague'][['City', 'AvgTemperatureCelsia']])

print(teplota[teplota['AvgTemperatureCelsia'] >= 30][['City','AvgTemperatureCelsia']])
print(teplota[(teplota['AvgTemperatureCelsia'] >= 15) & (teplota['Region'] == 'Europe')][['City','Day','AvgTemperatureCelsia']])
print(teplota[(teplota['AvgTemperatureCelsia'] >= 30) | (teplota['AvgTemperatureCelsia'] <= -10) ][['City','AvgTemperatureCelsia']])

# podezřelé hodnoty ??? nějak stejné.... -72.78, tj. je divné
print(teplota[teplota['AvgTemperatureCelsia'] <= -50][['City','AvgTemperatureCelsia']])