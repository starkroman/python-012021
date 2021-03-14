'''Uvažuj následující třídu Kontakt, která slouží k evidenci všech kontaktů (např. zákazníků,
zaměstnanců, uchazečů o práci atd.).'''

from datetime import datetime

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec(Kontakt):
    def get_info(self):
        datum = self.datum_pohovoru.strftime("%d.%m.%Y")
        return f"Uchazeč '{self.jmeno}' měl pohovor dne: {datum} se zápisem: {self.zapis_z_pohovoru}"

    def uloz_zapis(self, zapis):
        if self.datum_pohovoru > datetime.now():
            print("Pohovor ještě neproběhl. Nelze uložit zápas!")
            self.zapis_z_pohovoru = "Zatím není zápis."
        else:
            self.zapis_z_pohovoru = zapis

    def __init__(self, jmeno, email, datum_pohovoru):
        super().__init__(jmeno, email)
        self.datum_pohovoru = datum_pohovoru
        self.zapis_z_pohovoru = ""

petr = Uchazec("Petr Novák", "novakpe@czc.cz", datetime(2021,3,10))
print(petr.get_info())
petr.uloz_zapis("Prospěl výborně.")
print(petr.get_info())