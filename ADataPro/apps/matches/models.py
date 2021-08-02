import sys
from django.db import models
import sys
sys.path.append("./crawler_files/crawler_files/crawler_files/")
from startCrawling import startCrawling
from multiprocessing import Pool

# Create your models here.
class Matches(models.Model):
    team1_name = models.CharField('името на отбор', max_length=200)
    team2_name = models.CharField(max_length=200)
    date_match = models.DateTimeField()

def UpdateDB():
    pool = Pool(processes=1)
    pool.apply_async(startCrawling)
    pool.close()


class Teams():
    matches_list = Matches.objects.all()
    