from django.shortcuts import render

from .models import Matches, Teams, UpdateDB

def index(request):
    matches_list = Matches.objects.all()
    teams_list = []
    for a in matches_list.values():
        teams_list.append(a['team1_name'])
        teams_list.append(a['team2_name'])
    UpdateDB()
    return render(request, 'matches/index.html', {'matches_list': matches_list, 'teams_list': set(teams_list)})


def loadMatches(request):
    matches_list = Matches.objects.all()
    return render(request, 'matches/list.html', {'matches_list': matches_list})