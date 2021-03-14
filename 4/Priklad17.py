'''Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají.
Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani, který udává celkovou
délku pořadů, které uživatel zhlédl. Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.

- Třídám Serial a Film přidej funkce get_celkova_delka(), která vrátí celkovou délku filmu/seriálu
(u seriálu je to počet episod násobený délkou jedné episody).

- Třídě Uzivatel přidej funkci pripocti_zhlednuti(), která bude mít jeden parametr. Funkce zvýší
atribut udávající celkovou délku sledávní o zadaný parametr.

- Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci, že uživatel
zhlédne film a seriál, které jsi vytvořil(a) jako objekty. Uživateli připočti délky děl k délce sledování,
využij k tomu funkci get_celkova_delka() u objektu a seriálu, abys zjistil(a),
kolik minut (nebo hodin) videa celkem uživatel zhlédl.

- Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné a tuto
pomocnou proměnnou potom předáš jako parametr funkci pripocti_zhlednuti().'''

#
class Polozka:
    def get_info(self):
        return f"Položka: {self.nazev} je žánru: {self.zanr}."
    def add_zanr(self, novyZanr):
        self.zanr = novyZanr
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

class Film(Polozka):
    def get_celkova_delka(self):
        return self.delka

    def get_info(self):
        return f"{super().get_info()} Délka filmu je: {self.delka} min."
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka

class Serial(Polozka):
    def get_celkova_delka(self):
        return self.pocetEpizod * self.delkaEpizody

    def get_info(self):
        return f"{super().get_info()} Počet epizod je: {self.pocetEpizod} a délka epizody je: {self.delkaEpizody} min."

    def __init__(self, nazev, zanr, pocetEpizod, delkaEpizody):
        super().__init__(nazev, zanr)
        self.pocetEpizod = pocetEpizod
        self.delkaEpizody = delkaEpizody

class Uzivatel:
    def get_info(self):
        return f"Celková délka zhlédnutí uživatele {self.jmeno} je: {self.delkaSledovani} min."

    def pripocti_zhlednuti(self, pripoctiMinuty):
        self.delkaSledovani += pripoctiMinuty
        return self.delkaSledovani

    def __init__(self, jmeno, delkaSledovani = 0):  # můžu to takhle nadefinovat?? není to zbytečné??
        self.jmeno = jmeno
        self.delkaSledovani = delkaSledovani


film = Film("'Taková normální rodinka'", "'veselohra'", 60)
print(film.get_info())
print(f"Délka filmu je: {film.get_celkova_delka()} min.")

serial = Serial("'Ordinace v růžové zahradě'", "'totální blbost'", 100, 75)
print(serial.get_info())
print(f"Délka filmu je: {serial.get_celkova_delka()} min.")

franta = Uzivatel("Franta Bedla", film.get_celkova_delka() + serial.get_celkova_delka())
print(franta.get_info())
franta.pripocti_zhlednuti(200)
print(franta.get_info())