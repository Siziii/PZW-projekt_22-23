from django.contrib import admin
from .models import *

model_list = [Predmet, Ucenik, Profesor, Ucionica]
admin.site.register(model_list)
# Register your models here.
