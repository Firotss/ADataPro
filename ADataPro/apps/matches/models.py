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
    
    for list_of_matches in matches_list.values():
            teams_list.append(list_of_matches['team1_name'])
            teams_list.append(list_of_matches['team2_name'])
            
    return teams_list

def next_matches():
    matches_list = Matches.objects.all()
    weekend_list = []

    for list_of_matches in matches_list.values():
        time_now = timezone.now()
        first_match_date = list_of_matches['date_match']
        print(first_match_date, time_now-timezone.timedelta(days=3))
        if(first_match_date < time_now-timezone.timedelta(days=3)):
            continue

        for i in matches_list.values():
            match_date = i['date_match']
            if(match_date < first_match_date+timezone.timedelta(days=4) and match_date >= first_match_date):
                weekend_list.append(i)

        break

    return weekend_list

