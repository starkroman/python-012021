'''Stáhni si soubor character-deaths.csv, který obsahuje informace o smrti některých postav z prvních
pěti knih románové série Píseň ohně a ledu (A Song of Fire and Ice).
- Načti soubor do tabulky (DataFrame) a nastav sloupec Name jako index.
- Zobraz si sloupce, které tabulka má. Posledních pět sloupců tvoří zkratky názvů knih a informace o tom,
jestli se v knize postava vyskytuje.
- Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali".
- Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".
- Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year.
- Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom, v jakých knihách
se postava vyskytuje, tj. vypiš všechny sloupce mezi GoT a DwD.'''

import pandas as pd
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

kniha = pd.read_csv('character-deaths.csv')

# hlavička sloupců
print(kniha.head(n=0))
# indexace podle Name
kniha = kniha.set_index('Name')

# smrt postavy Hali - jako série
print(kniha.loc["Hali", "GoT":] == 0)
# smrt postavy Hali - jako DataFrame
print(kniha.loc[["Hali"], "GoT":])
# zobrazení řádků - jako série
print(kniha.loc["Gevin Harlaw":"Gillam"])
print(kniha.loc["Gevin Harlaw":"Gillam", "Death Year"])
print(kniha.loc["Gevin Harlaw":"Gillam", "GoT":])
#



