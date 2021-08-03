import sys
from django.db import models
from django.utils import timezone
from multiprocessing import Pool

sys.path.append("./crawler_files/crawler_files/crawler_files/")
from startCrawling import start_crawling


# Create your models here.
class Matches(models.Model):
    team1_name = models.CharField(max_length=200)
    team2_name = models.CharField(max_length=200)
    date_match = models.DateTimeField()

def update_db():
    pool = Pool(processes=1)
    pool.apply_async(start_crawling)
    pool.close()

class TeamsInfo(models.Model):
    matchID = models.IntegerField()
    team_name = models.CharField(max_length=200)
    wins = models.IntegerField()
    losses = models.IntegerField()
    draws = models.IntegerField()
    points = models.IntegerField()

def teams():
    matches_list = Matches.objects.all()
    teams_list = []
    weekend_list = []

    for a in matches_list.values():
        teams_list.append(a['team1_name'])
        teams_list.append(a['team2_name'])
        
        time_now = timezone.now()
        match_date = a['date_match']

        if(time_now.weekday() >= -6 and time_now.weekday() < -3):
            if(match_date > time_now and match_date < time_now+timezone.timedelta(days=4)):
                weekend_list.append(a)
        elif(match_date > time_now and match_date < time_now+timezone.timedelta(days=7)):
            weekend_list.append(a)

    return teams_list, weekend_list