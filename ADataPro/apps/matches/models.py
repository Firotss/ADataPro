import sys
from django.db import models
from django.utils import timezone
from datetime import datetime, time, timedelta
sys.path.append("./crawler_files/crawler_files/crawler_files/")
from startCrawling import startCrawling
from multiprocessing import Pool

# Create your models here.
class Matches(models.Model):
    team1_name = models.CharField(max_length=200)
    team2_name = models.CharField(max_length=200)
    date_match = models.DateTimeField()

def UpdateDB():
    pool = Pool(processes=1)
    pool.apply_async(startCrawling)
    pool.close()

class TeamsInfo(models.Model):
    matchID = models.IntegerField()
    team_name = models.CharField(max_length=200)
    wins = models.IntegerField()
    losses = models.IntegerField()
    draws = models.IntegerField()
    points = models.IntegerField()

def Teams():
    matches_list = Matches.objects.all()
    teams_list = []
    weekend_list = []
    for a in matches_list.values():
        teams_list.append(a['team1_name'])
        teams_list.append(a['team2_name'])
        now = timezone.now()
        if(now.weekday() >= -6 and now.weekday() < -3):
            if(a['date_match'] > now and a['date_match'] < now+timezone.timedelta(days=4)):
                weekend_list.append(a)
        elif(a['date_match'] > now and a['date_match'] < now+timezone.timedelta(days=7)):
            weekend_list.append(a)
    return teams_list, weekend_list