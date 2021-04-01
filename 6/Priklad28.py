'''
V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali.
Zkusme nyní zpracovat podobné úlohy pomocí pandas.

- Načti data ze souboru do tabulky.
- Vyfiltruj státy, které leží v Evropě.
- Zjisti počet států v jednotlivých subregionech Evropy.
- Zjisti cekový počet obyvatel v jednotlivých subregionech Evropy.
- Načti informace ze souborů do tabulek. Z tabulky s GDP odeber státy, které nemají kompletní informace
GDP (tj. ponech pouze státy, které mají kompletní data za všechny tři roky).
- Propoj obě tabulky podle třípísmenného kódu států.
- Spočti celkové HDP za rok 2019 a celkový počet obyvatel za jednotlivé subregiony.
- Projdi si subkapitolu o počítaných sloupcích (část o podmínených sloupcích není nutné číst). K tabulce, kterou jsi
vytovřila v předchozím kroku, vypočti GDP v roce 2019 na obyvatele, tj. přidej sloupec s velikostí GDP v roce 2019
vydělenou počtem obyvatel daného subregionu.
'''

import pandas as pd
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

staty = pd.read_json('staty.json')
#print(staty.head())

# státy ležící v Evropě
staty = staty[staty['region'] == 'Europe']
print(staty.head())

# zjistím si jednotlivé státy v regionech a subregionech Evropy  (sedí...53)
print(staty.groupby('region')['name'].count())
print(staty.groupby('subregion')['name'].count())

#celkový počet obyvatel v subregionech Evropy
print(staty.groupby('subregion')['population'].sum())

#bonus:
#gdp = pd.read_csv('gdp.csv')
#print(gdp.head())

# musím si opět načíst všechny státy
staty = pd.read_json('staty.json')

# vyčistíme DF -> gdp
gdp = pd.read_csv('gdp.csv').dropna()
print(gdp.head())

# propojíme obě tabulky podle třípísmenk. kódu => alpha3Code
gdp = gdp.rename(columns={'Country Code' : 'alpha3Code'})

# spojíme si obě tabulky
staty_s_gdp = pd.merge(staty, gdp, how='left')

# kontrola joinu
print(staty.shape)
print(staty_s_gdp.shape)

#Celkové HDP z rok 2019
staty_hdp_2019 = staty_s_gdp['2019'].sum()
print(f"Celkové HDP z rok 2019: {staty_hdp_2019}")

# jenom součet populace
print(staty.groupby('subregion')['population'].sum())

# spojím to dohromady
staty_subreg_hdp_2019 = staty_s_gdp.groupby('subregion')[['population','2019']].sum()
print(staty_subreg_hdp_2019.head())

# více různých agregací (navíc...)
staty_agg = staty.groupby("subregion").agg({'population' : ['sum', 'mean']})
print(staty_agg.head())

# počítané sloupce:
staty_subreg_hdp_2019['gdp_na_pocet_obyvatel'] = round(staty_subreg_hdp_2019['2019'] / staty_subreg_hdp_2019['population'],2)
print(staty_subreg_hdp_2019.head())