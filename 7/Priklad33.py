'''Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020.
Soubor obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.

- Vytvoř čárový graf vývoje zavírací ceny akcie (sloupec Close) v čase.
- Převeď sloupec Date na typ Datetime příkazem níže a vytvoř stejný graf jako předtím.
Porovnej grafy a zjisti, co se změnilo.
- Přidej ke grafům popisky os a titulky. Po zavolání funkce plot() si výsledek ulož do proměnné ax.
Následně zavolej metodu set_ylabel(), abys nastavila popisek osy y grafu.
- Obdobně využij metody set_title() a set_xlabel() a nastav popisek osy x a titulek grafu.
'''

import pandas
import matplotlib.pyplot as plt

import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

twilio = pandas.read_csv("twlo.csv")
twilio = twilio.set_index('Date')
#print(twilio.head())

ax = twilio['Close'].plot(grid=True)
ax.set_ylabel('Cena v dolarech')
ax.set_xlabel('Datum')
ax.set_title('Akcie firmy TWILIO  - 2020/03-2021')
plt.show()

import datetime
twilio = pandas.read_csv("twlo.csv")
twilio["Date"] = pandas.to_datetime(twilio["Date"])
twilio = twilio.set_index('Date')
print(twilio.head())
ax = twilio['Close'].plot(grid=True)
ax.set_ylabel('Cena v dolarech')
ax.set_xlabel('Datum')
ax.set_title('Akcie firmy TWILIO  - 2020/03-2021')
plt.show()
