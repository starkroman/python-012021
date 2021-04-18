from django.db import models

# Create your models here.
class Auto(models.Model):
    znackaReg = models.CharField(max_length=20)
    typAuta = models.CharField(max_length=30)
    pocetKM = models.IntegerField()
    datumPoslSTK = models.DateField()

class Zakaznik(models.Model):
    jmenoPrijmeni = models.CharField(max_length=100)
    cisloRidicaku = models.CharField(max_length=15)
    datumNarozeni = models.DateField()

class Vypujcka(models.Model):
    datumCasZacatkuVypujcky = models.DateTimeField()
    datumCasKonceVypujcky = models.DateTimeField()
    cenaVypujcky = models.IntegerField()