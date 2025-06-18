from django.db import models

# Create your models here.


class Pokemon(models.Model):
    order = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    hp = models.IntegerField()
    atk = models.IntegerField()
    spatk = models.IntegerField()
    defense = models.IntegerField()
    spdef = models.IntegerField()
    speed = models.IntegerField()