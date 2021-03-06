class Auto:
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

# kontrola, aby se nedalo půjčit 2x
print(auto2.get_info())
print(auto2.pujc_auto())
print(auto2.pujc_auto())
print(auto2.get_info())


typAuta = input("Vyber typ auta pro zapůjčení -> [Peugeot/Škoda]: ").lower()
if typAuta in ["peugeot", "skoda", "škoda"]:
    if typAuta == "peugeot" and auto1.volne:
        print(auto1.get_info())
        print(auto1.pujc_auto())
    elif ["skoda", "škoda"] and auto2.volne:
        print(auto2.get_info())
        print(auto2.pujc_auto())
    else:
        print("Auto je zapůčené!")
else:
    print("Takové auto nemáme na skladě!")


