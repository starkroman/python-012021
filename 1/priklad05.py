'''Nakladatel má nyní v software dva slovníky, které obsahují informace o prodejích knih v letech 2019 a 2020.
Uvažuj, že uživatel se zajímá o prodeje konkrétní knihy. Zeptej se uživatele na název knihy a poté vypiš informaci
 o tom, kolik se této knihy celkem prodalo. Nezapomeň na to, že některé knihy byly prodávány pouze v jednom roce.'''

prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Zločinný steh": 5412,
    "Past": 2364,
    "Zkus mě chytit": 6671,
}

pocetKnih = 0
nazevKnihy = input("Zadej název knihy: ")
if nazevKnihy in prodeje2019:
    pocetKnih += prodeje2019[nazevKnihy]
if nazevKnihy in prodeje2020:
    pocetKnih += prodeje2020[nazevKnihy]
print(f"Počet knih s názven \"{nazevKnihy}\" bylo prodáno celkem: {pocetKnih} ks.")
