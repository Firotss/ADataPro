from django.db import models

# Create your models here.
class Matches(models.Model):
    team1_name = models.CharField('името на отбор', max_length=200)
    team2_name = models.CharField(max_length=200)
    date_match = models.CharField(max_length=200)