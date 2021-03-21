'''Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020.
Soubor obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.
- Zjisti, kolik má soubor řádek a kolik sloupců.
- U akcií nás zajímají především nejnovější ceny. Podívej se na poslední řádek souboru.
- Podívej se na 5 řádků s cenami na začátku souboru, využij k tomu funkci iloc i funkci head().
Tentokrát využij způsob dle vlastního výběru:
- Počet řádků ulož do proměnné pocet_radku jako číslo.
- Pokud funkci iloc zadáš číslo řádku i číslo sloupce, odkazuješ se na jednu konkrétní hodnotu.
Pandas ti tuto hodnotu vrací jako číslo. Načti si tedy první hodnotu zavírací ceny (sloupec Close)
v souboru a poslední hodnotu zavírací ceny v souboru. Vypočítej, o kolik procent se zvýšila hodnota akcie.
- Vyber si sloupec s maximální cenou akcie (sloupec High) za jednotlivé dny pomocí loc nebo iloc jako sérii.
Na sloupec použij funkci .max(), abys zjistila maximální zaznamenanou cenu akcie za celé období.
Obdobným způsobem použij funkci .min() na sloupec Low. Z těchto hodnot zjistíš maximální rozsah obchodní
ceny akcie, což je základ jednoho z akciových ukazatelů (price range).'''

import pandas as pd
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

akcieTWLO =  pd.read_csv('twlo.csv')

# varianta:
print("Řákdů má: " + str(akcieTWLO.shape[0]))
print("Sloupečků má: " + str(akcieTWLO.shape[1]))

# poslední řádky souboru
print(akcieTWLO.tail(n=1))
# nebo poslední řádek souboru
print(akcieTWLO[301:])

# prvních pět řádků souboru jako DataFrame
print(akcieTWLO.head())
print(akcieTWLO.head(n=5))
print(akcieTWLO.iloc[:5])

# varianta: počet řádků v proměnné
pocet = akcieTWLO.shape
print(f"Soubor má:  {pocet[0]} řádků a {pocet[1]} sloupečků.")

# výpočet
procento = round((akcieTWLO["Close"][301] * 100)/akcieTWLO["Close"][0],1)
print(f"Nárůst je o: {procento} %")

# maximální cena akcie
maxCenaAkcie = akcieTWLO['High']
print("MAX:",maxCenaAkcie.max())

# minimální cena akcie
minCenaAkcie = akcieTWLO['Low']
print("MIN:",minCenaAkcie.min())

# rozsah obchodní ceny akcie
price_range = maxCenaAkcie.max() - minCenaAkcie.min()
print("Rozsah obchodní ceny akcie je: " + str(round(price_range,2)) + " Kč.")

#
maxPoDruhe = akcieTWLO.iloc[:,3]
print("MAX2:" + str(maxPoDruhe.max()))

minPoDruhe = akcieTWLO.iloc[:,4]
print("MIN2:{0}".format(str(minPoDruhe.min())))

# 2. rozsah obchodní ceny akcie
price_range = maxPoDruhe.max() - minPoDruhe.min()
print("Rozsah obchodní ceny akcie je: " + str(round(price_range,2)) + " Kč.")


# toto je moje výuková část:
# řádek na pozici 3 jako série
print(akcieTWLO.iloc[3])
# řádek na pozici 3 jako DataFrame
print(akcieTWLO.iloc[[3]])
# řádky na pozicích....1,3,5,7
print(akcieTWLO.iloc[[1,3,5,7]])
# řádky 1 až 4, sloupce 2 a výše
print(akcieTWLO.iloc[1:4, 2:])
# zjistit jeden konkrétní údaj
print(akcieTWLO.iloc[3,3])
# zjistit si jeden celý 3.sloupec
print(akcieTWLO.iloc[:,3])

# můžu uložit jako: csv, json, html, ...
#akcieTWLO.to_html('akcieTWLO.html')
#akcieTWLO.to_json('akcieTWLO.json')