from django.db import models

class Rang(models.Model):
    nomi = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nomi

class Gul(models.Model):
    nomi = models.CharField(max_length=20)
    rangi = models.ForeignKey(Rang, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.nomi

class Osimlik(models.Model):
    nomi = models.CharField(max_length=20)
    rangi = models.ForeignKey(Rang, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nomi 