class Auto:
    def __init__(self, spz, typ, pocetKm):
        self.spz = spz
        self.typ = typ
        self.pocetKm = pocetKm
        self.volne = True

    def get_info(self):
        return f"Typ: {self.typ}, SPZ: {self.spz}, Počet najetých km: {self.pocetKm}, Stav: {self.volne}"

auto1 = Auto("4A2 3020", "Peugeot 403 Clio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253 )

print(auto1.get_info())
print(auto2.get_info())

