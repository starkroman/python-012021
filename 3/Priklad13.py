class Auto:
    def vrat_auto(self, stavTachometru, pocetDniPouzivani):
        self.stavTachometru = stavTachometru
        self.volne = False
        #
        cenaZaPujceni = 0
        if pocetDniPouzivani >= 0:
            if pocetDniPouzivani <= 7:
                cenaZaPujceni = pocetDniPouzivani * 400
            else:
                cenaZaPujceni = pocetDniPouzivani * 300
            return cenaZaPujceni
        else:
            return f"Chybný údaj o počtu dní."

    def pujc_auto(self):
        if not self.volne:
            return f"Vozidlo není k dispozici."
        else:
            self.volne = False
            return f"Potvrzuji zapůjčení vozidla."

    def get_info(self):
        return f"Typ: {self.typ}, SPZ: {self.spz}, Počet najetých km: {self.pocetKm}, Stav: {self.volne}"

    def __init__(self, spz, typ, pocetKm):
        self.spz = spz
        self.typ = typ
        self.pocetKm = pocetKm
        self.volne = True

auto1 = Auto("4A2 3020", "Peugeot 403 Clio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253 )


kolikKmUjeto = float(input("Zadej počet ujetých km: "))
jakDlouhoByloZapujceno = int(input("Zadej počet dní zapůjčení vozidla: "))
if jakDlouhoByloZapujceno > 0:
    print(f"Cena za zapůjčení vozidla: {auto1.vrat_auto(kolikKmUjeto, jakDlouhoByloZapujceno)} Kč." )
else:
    print(f"Chybný údaj v počtu dní zapůjčení!")


