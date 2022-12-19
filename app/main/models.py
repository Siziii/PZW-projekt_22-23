from django.db import models


class Profesor(models.Model):
    profesor_ime = models.CharField(max_length=100)
    profesor_prezime = models.CharField(max_length=100)
    profesor_placa = models.PositiveIntegerField()
    class Meta:
        verbose_name_plural = "Profesori"
    def __str__(self):
        return f"{self.profesor_ime} {self.profesor_prezime}"


class Ucionica(models.Model):
    
    ucionica_broj = models.PositiveIntegerField()
    ucionica_kvadratura = models.PositiveIntegerField()
    def __str__(self):
        return f"Ucionica {self.ucionica_broj}"
    class Meta:
        verbose_name_plural = "Ucionice"

class Predmet(models.Model):
    predmet_naziv = models.CharField(max_length=100)
    predmet_opis = models.TextField()
    predmet_predavac = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    ucionica = models.OneToOneField(
        Ucionica,
        on_delete=models.CASCADE,
        default = "0",
        primary_key=True,
    )
    class Meta:
        verbose_name_plural = "Predmeti"
        verbose_name = "Predmet"
    def __str__(self):
        return f"{self.predmet_naziv}"

class Ucenik(models.Model):
    ucenik_ime = models.CharField(max_length=100)
    ucenik_prezime = models.CharField(max_length=100)
    ucenik_predmeti = models.ManyToManyField(Predmet)
    ucenik_razrednik = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ucenik_ime} {self.ucenik_prezime}"
    class Meta:
        verbose_name_plural = "Ucenici"


 

# Create your models here.
