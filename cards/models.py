from django.db import models
from django.contrib.auth import models as auth_models


class Card(models.Model):
  name = models.CharField(max_length=200)
  types = models.CharField(max_length=100)
  supertypes = models.CharField(max_length=100)
  manaValue = models.IntegerField(blank=True)
  colorIdentity = models.CharField(max_length=50)
  rarity = models.CharField(max_length=100)
  keywords = models.CharField(max_length=200)
  power = models.IntegerField(blank=True, null=True)
  toughness = models.IntegerField(blank=True, null=True)
  text = models.TextField(default='')
  scryfallId = models.CharField(max_length=200)
  users = models.ManyToManyField(auth_models.User)
  

  def __str__(self):
        return f"Card: {self.name} Types: {self.types} Supertypes: {self.supertypes} ManaValue: {self.manaValue} Colors: {self.colorIdentity} Rarity: {self.rarity}"


class Deck(models.Model):
  name = models.CharField(max_length=200)
  user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
  cards =  models.ManyToManyField(Card)
  
  def __str__(self):
    return self.name




