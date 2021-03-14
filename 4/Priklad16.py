'''Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa. Služba nabízí dva typy pořadů
- filmy a seriály. Firma chce evidovat, které filmy a seriály nabízí a jejich žánry. Dále chce u filmů
evidovat délku a u seriálů počet episod a délku jedné episody.

- Vytvoř program, který bude obsahovat tři třídy - Polozka, Film a Serial.
- Třída Polozka bude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr.
Oba atributy nastav ve funkci __init__(), žánr získej jako parametr funkce.
- Třída Film bude potomkem třídy Polozka. Film má kromě názvu a žánru atribut délka.
- Třída Serial bude potomkem třídy Polozka. Má kromě názvu a žánru atributy počet epizod a délka epizody.
Všem třídám přidej funkci get_info(), která vypíše informace o položce, resp. o filmu a seriálu.
Funkce u třídy Polozka vypíše název a žánr. Následně tuto funkci využij ve funkcích u tříd Film a
Serial a přidej k ní informaci o délce, resp. počtu episod.'''

class Polozka:
    def get_info(self):
        return f"Položka: {self.nazev} je žánru: {self.zanr}."
    def add_zanr(self, novyZanr):
        self.zanr = novyZanr
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

class Film(Polozka):
    def get_info(self):
        return f"{super().get_info()} Délka filmu je: {self.delka} min."
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka

class Serial(Polozka):
    def get_info(self):
        return f"{super().get_info()} Počet epizod je: {self.pocetEpizod} a délka epizody je: {self.delkaEpizody} min."

    def __init__(self, nazev, zanr, pocetEpizod, delkaEpizody):
        super().__init__(nazev, zanr)
        self.pocetEpizod = pocetEpizod
        self.delkaEpizody = delkaEpizody

#
polozka = Polozka("'Čtyři vraždy stačí, drahoušku'", "'komedie'")
print(polozka.get_info())
polozka.add_zanr("'super_komedie'")
print(polozka.get_info())

film = Film("'Taková normální rodinka'", "'veselohra'", 60)
print(film.get_info())

serial = Serial("'Ordinace v růžové zahradě'", "'totální blbost'", 1500, 75)
print(serial.get_info())