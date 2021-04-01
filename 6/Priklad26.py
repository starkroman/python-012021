'''
Máme softwarovou firmu. Firma má kanceláře v Praze, Plzni a Liberci. Seznam zaměstnanců pro jednotlivé
kanceláře najdeš v souborech zam_praha.csv, zam_plzeň.csv a zam_liberec.csv.

- Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
- Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
- Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.
- Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.
- Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.
- Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
- V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují.
- Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV.

'''

import pandas as pd
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

praha = pd.read_csv('zam_praha.csv')
print(praha.head())
plzen = pd.read_csv('zam_plzeň.csv')
liberec = pd.read_csv('zam_liberec.csv')

# přidám do každégo DF nový sloupec mesto (ztratil jsem tuto informaci...)
praha['mesto'] = 'Praha'
plzen['mesto'] = 'Plzeň'
liberec['mesto'] = 'Liberec'
# např. jen jak to vypadá... kontrolní tisk
print(liberec)

# nová tabulka zamestnanci s "přeindexováním!!!
zamestnanci = pd.concat([praha, plzen, liberec], ignore_index=True)
print(zamestnanci.shape)

# můžu si výsledek uložit do externího csv souboru bez indexu
# zamestnanci.to_csv('zamestnanci.csv', index=False)

# načtu si soubor s platy...
platy = pd.read_csv('platy_2021_02.csv')

# spojíme s další tabulkou - platy...
zamestnanci_s_platy = pd.merge(zamestnanci, platy)
print(zamestnanci_s_platy.shape)   # doplnil platy jen u 43 zaměstnanců

# průměrný plat v jednotlivých pobočkách
print(round(zamestnanci_s_platy.groupby('mesto')['plat'].mean()))

# výčet zaměstnanců, kteří ve firmě již nepracují
zamestnanci_s_platy_2 = pd.merge(zamestnanci, platy, how='left')
print(zamestnanci_s_platy_2)

# výčet zamestnanců, kde plat => NaN
zamestnanci_s_platy_3 = zamestnanci_s_platy_2[zamestnanci_s_platy_2['plat'].isnull()]
print(zamestnanci_s_platy_3)

# uložím si výsledek do csv souboru
zamestnanci_s_platy_3.to_csv('seznamJizNepracujicichZamestnancu.csv', index=False)

# počet zaměstnanců, kteří ve firmě již nepracují
pocet = zamestnanci_s_platy_3['prijimeni'].count()
print(f"Počet již nepracujících zaměstnanců ve firmě: {pocet}.")







