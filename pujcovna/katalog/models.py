from django.db import models

# !!! Záleží na pořadí !!!
class Zakaznik(models.Model):
    jmenoPrijmeni = models.CharField(max_length=100)
    cisloRidicaku = models.CharField(max_length=15)
    datumNarozeni = models.DateField()

    def __str__(self):
        return self.jmenoPrijmeni


class Auto(models.Model):
    znackaReg = models.CharField(max_length=20)
    typAuta = models.CharField(max_length=30)
    pocetKM = models.IntegerField()
    datumPoslSTK = models.DateField()
    zakaznik = models.ForeignKey('Zakaznik', on_delete=models.SET_NULL, null=True)
    # zde může být jak Zakaznik, tak 'Zakaznik' (v apostrofech, kvůli pořadí)

    def __str__(self):
        return self.znackaReg + ": " + self.typAuta


class Vypujcka(models.Model):
    datumCasZacatkuVypujcky = models.DateTimeField()
    datumCasKonceVypujcky = models.DateTimeField()
    cenaVypujcky = models.IntegerField()
    auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.auto.__str__()


