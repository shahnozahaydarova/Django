from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Home(models.Model):
    contant = models.CharField(max_length=250)
    data = models.DateField(auto_now_add=True)
    img = models.CharField(max_length=255)
    name = models.ForeignKey(Name,on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return self.contant