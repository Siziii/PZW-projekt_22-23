from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from main.models import Profesor, Ucenik, Ucionica, Predmet

## Create your views here.
def homepage(request):
    return HttpResponse('Welcome to homepage! <strong>#samoOIRI</strong>')
    # primjetiti korištenje HTML-a






class ProfesorList(ListView):
    model = Profesor


class UcenikList(ListView):
    model = Ucenik



class UcionicaList(ListView):
    model = Ucionica


class PredmetList(ListView):
    model = Predmet
