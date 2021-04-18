from django.shortcuts import render
import datetime

# Create your views here.
from django.views import View
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
        return HttpResponse('<h1>Vítejte v naší půjčovně!</h1>'
                            '<a href=http://localhost:8000/katalog/seznam/>Jaká máte auta?</a>'
                            '<br><h2>O naší půjčovně</h2><p>Naše půjčovna vznikla v roce '
                            '2011 a dnes nabízí přibližně 30 aut.</p>')

class SeznamView(View):
    def get(self, request):
        return HttpResponse("Zde bude seznam aut!")
