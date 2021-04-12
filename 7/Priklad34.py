'''Ze souboru velikonoce.csv načti data o tom, kolikrát na který datum připadaly Velikonoce v letech 1600 až 2100.
- Vytvoř sloupcový graf, který data přehledně zobrazí. Na ose x budou vidět jednotlivá data ("datumy")
a výška sloupce označí, kolikrát na daný den připadly Velikonoce.

bonus:
-Vytvoř si datový soubor sama. Můžeš k tomu využít modul dateutil, který při instalaci najdeš pod jménem python-dateutil.
Následně si zkopíruj kód níže a doplň na místo komentářů příkazy, které prováději požadovanou činnost.

'''

import wget
import pandas as pd
import pytemperature
import matplotlib.pyplot as plt

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

velikonoce = pd.read_csv('velikonoce.csv')
print(velikonoce.head())
velikonoce = velikonoce.set_index('Datum')

ax = velikonoce['Počet'].plot(kind='bar', grid=True)
ax.set_ylabel('Počet dnů')
ax.set_xlabel('Datum')
ax.set_title('Velikonoce od 1600 do 2100')
plt.show()

#bonus  (nevím co to má dělat???)

from dateutil import easter

data = []
for rok in range(2000,2022):
  datum = easter.easter(rok).strftime("%m-%d")
  data.append(datum)

data = pd.DataFrame(data, columns=["Datum"])
#print(data.head(n=10))
data = data.groupby("Datum").size()
print(data)