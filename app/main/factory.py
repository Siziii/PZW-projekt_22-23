import factory
from factory.django import DjangoModelFactory
from factory import RelatedFactoryList
import factory.fuzzy
from main.models import *
import random

## Defining a factory
class ProfesorFactory(DjangoModelFactory):
    class Meta:
        model = Profesor

    profesor_ime = factory.Faker("first_name")
    profesor_prezime = factory.Faker("last_name")
    profesor_placa = factory.fuzzy.FuzzyInteger(8000, 12000)


class PredmetFactory(DjangoModelFactory):
    class Meta:
        model = Predmet
    predmet_naziv = factory.Iterator(["Matematika","Hrvatski","Engleski","Tjelesna i zdravstvena", "Priroda i društvo", "Povijest","Geografija","Fizika","Biologija","Tehnička kultura","Likovna kultura","Kemija"])
    predmet_opis = factory.Faker("sentence", nb_words=20)
    predmet_predavac = factory.Iterator(Profesor.objects.all())

class UcenikFactory(DjangoModelFactory):
    class Meta:
        model = Ucenik
    ucenik_ime = factory.Faker("first_name")
    ucenik_prezime = factory.Faker("last_name")
    ucenik_razrednik = factory.Iterator(Profesor.objects.all())

class UcionicaFactory(DjangoModelFactory):
    class Meta:
        model = Ucionica
    predmet = factory.SubFactory(PredmetFactory)
    ucionica_broj = factory.Sequence(lambda n : "{}".format(n+1))
    ucionica_kvadratura = factory.fuzzy.FuzzyInteger(50, 80)
