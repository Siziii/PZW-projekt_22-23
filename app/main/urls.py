from django.urls import path
from . import views
from main.views import ProfesorList, UcenikList, UcionicaList, PredmetList

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('profesori/', ProfesorList.as_view()),
    path('ucenici/', UcenikList.as_view()),
    path('ucionice/', UcionicaList.as_view()),
    path('predmeti/', PredmetList.as_view()),
]