from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    #path("seznam/", views.SeznamView.as_view(), name='seznam'),
    path("seznam/", views.AutoView.as_view(), name='auto'),
    path("vypujcka/", views.VypujckaView.as_view(), name='vypujcka'),
    path("zakaznici/", views.ZakazniciView.as_view(), name = 'zakaznici'),
    path("seznam/<int:pk>", views.DetailAuto.as_view(), name='detail_auto'),
    path("vypujcka/<int:pk>", views.DetailVypujcky.as_view(), name='detail_vypujcka'),
    path("zakaznici/<int:pk>", views.DetailZakaznika.as_view(), name='detail_zakaznici'),
    path("noveAuto/", views.ZadejNoveAuto.as_view(), name='zadej_nove_auto'),
    path("noveAuto/", views.PotvrditNoveAuto.as_view(), name='potvrdit_nove_auto'),
    path("novyZakaznik/", views.ZadejNovehoZakaznika.as_view(), name='novy_zakaznik'),
    path("novyZakaznik/", views.PotvrditNovehoZakaznika.as_view(), name='potvrdit_noveho_zakaznika'),
]