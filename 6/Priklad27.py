'''
Pokračuj ve své práci pro softwarovou firmu. Ze souboru vykazy.csv načti informace o výkazech na projekty
pro jednoho vybraného zákazníka.

- Načti data ze souboru a ulož je do tabulky.
- Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.
- Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení.
- Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře, tj. spočítej celkový počet hodin
vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.
'''

import pandas as pd
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

# načítám z minulého projektu + výkazy (opravil jsem si jméno sloupečku, aby to bylo stejné...)
zamestnanci = pd.read_csv('zamestnanci.csv')
vykazy = pd.read_csv('vykazy.csv')
print(vykazy.head())

# musím si přejmenovat sloupeček, aby to "hrálo spolu..."
vykazy = vykazy.rename(columns={'emloyee_id' : 'cislo_zamestnance' })

# join tabulek
zamestnanci_s_vykazy = pd.merge(zamestnanci,vykazy)
print(zamestnanci_s_vykazy.head())

# celkový počet vykázaných hodin za projekty
print(zamestnanci_s_vykazy.groupby('project')['hours'].sum())

# počet vykázaných hodin za jednotlivé kanceláře
print(zamestnanci_s_vykazy.groupby('mesto')['hours'].sum())

# uložení do excelu
zamestnanci_s_vykazy = zamestnanci_s_vykazy.groupby('mesto')['hours'].sum()
zamestnanci_s_vykazy.to_excel('celkem.xlsx')


