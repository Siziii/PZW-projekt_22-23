from django.shortcuts import render
from django.views.generic import ListView
from main.models import Profesor, Ucenik, Ucionica, Predmet

def homepage(request):
    return render(request, "homepage.html")

class ProfesorList(ListView):
    model = Profesor

class UcenikList(ListView):
    model = Ucenik

class UcionicaList(ListView):
    model = Ucionica

class PredmetList(ListView):
    model = Predmet
