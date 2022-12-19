import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Profesor, Ucenik, Predmet, Ucionica
from main.factory import (
    ProfesorFactory,
    UcenikFactory,
    PredmetFactory,
    UcionicaFactory
)

NUM_PROFESORI = 15
NUM_UCENICI = 50
NUM_UCIONICE = 12

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Profesor, Ucenik, Predmet, Ucionica]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_PROFESORI):
            profesor = ProfesorFactory()
        for _ in range(NUM_UCENICI):
            ucenik = UcenikFactory()
        for _ in range(NUM_UCIONICE):
            ucionica = UcionicaFactory()