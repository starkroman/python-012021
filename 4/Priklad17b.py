'''V pokročilejší variantě neeviduj pouze délku sledování ale i to, jaké pořady uživatel sledoval.
Namísto délky sledování vytvoř atribut, který bude udávat zhlédnuté pořady (ideální pro tento účel
je seznam). Dále přidej funkci zhledni_polozku(), která do seznamu zhlédnutých pořadů přidánovou položku.

Dále vytvoř funkci delka_sledování() pro uživatele, která projde položky v seznamu a vrátí celkovou
délku všech pořadů, které uživatel zhlédl.'''

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
        vystup = f"{self.jmeno} zkouknul tyto pořady:"
        for porad in self.seznamSledovani:
            vystup += porad.self.jmeno + ", jehož žánr je: " + porad.self.zanr
        return vystup

    def add_polozku(self, novyPorad):
        self.seznamSledovani.append(novyPorad)

    def get_delka_sledovani(self):
        delkaSledovanani = 0

    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.seznamSledovani = []



franta = Uzivatel("Franta Bubla")
print(franta.get_info())
franta.add_polozku(Film("Motýlek", "drama", 120))
print(franta.get_info())

