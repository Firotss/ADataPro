from django.db.models.aggregates import Sum
from django.shortcuts import render
from .models import Matches, Teams, TeamsInfo, UpdateDB
from django.db.models import Count, query

def index(request):
    matches_list = Matches.objects.all()
    teams_list, weekend_list = Teams()
    UpdateDB()
    return render(request, 'matches/list.html', {'matches_list': matches_list, 
    'teams_list': set(teams_list), 'weekend_list': weekend_list})


def search(request, id):
    matches_list = Matches.objects.all()
    teams_list, weekend_list = Teams()

    ranking_list = TeamsInfo.objects.values('team_name').annotate(
    wins=Sum('wins'), losses=Sum('losses'), draws=Sum('draws'), points=Sum('points')
    ).order_by('wins', 'draws', 'points').reverse()
    
    if id == '0':
        return render(request, 'matches/list.html', {'list':matches_list, 'teams_list': set(teams_list)})
    if id == '1':
        return render(request, 'matches/list.html', {'list':weekend_list, 'teams_list': set(teams_list)})
    if id == '2':
        return render(request, 'matches/ranking.html', {'list':ranking_list, 'teams_list': set(teams_list)})

    searched_team = []
    for a in matches_list.values():
        if(a['team1_name'] == id or a['team2_name'] == id):
            searched_team.append(a)

    return render(request, 'matches/list.html', {'list':searched_team, 'teams_list': set(teams_list)})