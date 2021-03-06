from datetime import datetime, timedelta

prvni_datum = datetime(2021, 7, 1)
druhe_datum = datetime(2021, 8, 10)
treti_datum = datetime(2021, 8, 11)
ctvrte_datum = datetime(2021, 8, 31)

datum = input("Zadej datum: ")
datum = datetime.strptime(datum, "%d.%m.%Y")

pomocna = 0
if (datum >= prvni_datum and datum <= druhe_datum):
    pomocna = 1
elif (datum >= treti_datum and datum <= ctvrte_datum):
    pomocna = 2
else:
    print("Středisko je v tomto termínu zavřené!")
    exit()

pocetOsob = int(input("Zadej počet osob: "))
if pomocna == 1:
    cenaListku = pocetOsob * 250
else:
    cenaListku = pocetOsob * 180
print(f"Cena za lístky je: {cenaListku} Kč.")