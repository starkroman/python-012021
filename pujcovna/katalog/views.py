from django.shortcuts import render
import datetime

from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView, TemplateView
from . import models
# reverse - přidat
from django.urls import reverse_lazy

# indexView
class IndexView(View):
    def get(self, request):
        return HttpResponse(
        '<h1>Vítejte v naší půjčovně!</h1>'
        '<h2>O nás</h2>'
        '<p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>'
        '<br><hr>'
        '<li><a href=http://localhost:8000/katalog/seznam/>Jaká máte auta?</a></li>'
        '<br>'
        '<li><a href=http://localhost:8000/katalog/vypujcka/>Seznam vypůjčených aut</a></li>'
        '<br><hr>'
        '<li><a href=http://localhost:8000/katalog/zakaznici/>Seznam našich zákazníků</a></li>'
        '<br>'
        '<li><a href=http://localhost:8000/katalog/noveAuto/>Vložit nové auto</a></li>'
        '<br>'
        '<li><a href=http://localhost:8000/katalog/novyZakaznik/>Vložit nového zákazníka</a></li>'
        )

class SeznamView(View):
    def get(self, request):
        return HttpResponse("Zde bude seznam aut!")

'''------------------------------------------------'''
# pohledy
class AutoView(ListView):
    model = models.Auto
    template_name = 'katalog/auto2_list.html'

class VypujckaView(ListView):
    model = models.Vypujcka
    template_name = 'katalog/vypujcka_list.html'

class ZakazniciView(ListView):
    model = models.Zakaznik
    template_name = 'katalog/zakaznici_list.html'

'''---------------------------------------------'''
#detaily
class DetailAuto(DetailView):
    model = models.Auto
    template_name = 'katalog/detail_auto.html'

class DetailVypujcky(DetailView):
    model = models.Vypujcka
    template_name = 'katalog/detail_vypujcky.html'

class DetailZakaznika(DetailView):
    model = models.Zakaznik
    template_name = 'katalog/detail_zakaznik.html'

'''----------------------------------------------'''
# formuláře
class ZadejNoveAuto(CreateView):
    model = models.Auto
    template_name = 'noveAuto/nove_auto.html'
    fields = ['znackaReg', 'typAuta', 'pocetKM', 'datumPoslSTK', 'zakaznik']
    # nutno ještě přidat na závěr
    success_url = reverse_lazy('potvrdit_nove_auto')

class PotvrditNoveAuto(TemplateView):
    template_name = 'noveAuto/potvrdit_auto.html'

class ZadejNovehoZakaznika(CreateView):
    model = models.Zakaznik
    template_name = 'novyZakaznik/novy_zakaznik.html'
    fields = ['jmenoPrijmeni', 'cisloRidicaku', 'datumNarozeni']
    success_url = reverse_lazy('potvrdit_noveho_zakaznika')

class PotvrditNovehoZakaznika(TemplateView):
    template_name = 'novyZakaznik/potvrdit_noveho_zakaznika.html'