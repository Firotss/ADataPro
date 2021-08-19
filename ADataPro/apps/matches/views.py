from django.db.models.aggregates import Sum
from django.shortcuts import render
from .models import Matches, teams, TeamsInfo, update_db, next_matches
from django.utils import timezone
from django.views.generic import TemplateView

class Index(TemplateView):
    def get(self, request):
        matches_list = Matches.objects.all()
        teams_list = teams()
        update_db()

        return render(request, 'matches/list.html', 
                        {'list': matches_list, 
                        'teams_list': set(teams_list)})

class Search(TemplateView):
    def get(self, request, id):
        matches_list = Matches.objects.all().filter(year = int(timezone.now().year))
        teams_list = teams()
        
        if id == 'all_matches':
            return render(request, self.template_name, {'list':matches_list, 'teams_list': set(teams_list)})
        if id == 'next_matches':
            weekend_list = next_matches()
            return render(request, self.template_name, {'list':weekend_list, 'teams_list': set(teams_list)})
        
        searched_team = []
        for actual_teams_list in matches_list.values():
            if(actual_teams_list['team1_name'] == id or actual_teams_list['team2_name'] == id):
                searched_team.append(actual_teams_list)
        
        return render(request, self.template_name, {'list':searched_team, 'teams_list': set(teams_list)})
        
class SearchByYear(TemplateView):
    def get(self, request, team_id, year_id):
        matches_list = Matches.objects.all().filter(year = int(year_id))
        teams_list = teams()

        searched_team = []
        for actual_teams_list in matches_list.values():
            if(actual_teams_list['team1_name'] == team_id or actual_teams_list['team2_name'] == team_id):
                searched_team.append(actual_teams_list)
        
        return render(request, self.template_name, {'list':searched_team, 'teams_list': set(teams_list)})
    
class TeamsList(TemplateView):
    def get(self, request, id):
        teams_list = teams()
        matches_list = Matches.objects.all().filter(year = int(id))
        return render(request, self.template_name, {'list':matches_list, 'teams_list': set(teams_list)})

class RankingOrAllMatches(TemplateView):
    def get(self, request, id):
        teams_list = teams()
        if(self.template_name == "matches/list.html"):
            matches_or_ranking_list = Matches.objects.all().filter(year = int(id))
        else:
            matches_or_ranking_list = TeamsInfo.objects.filter(date = int(id)).values('team_name').annotate(
                                    wins=Sum('wins'), losses=Sum('losses'), 
                                    draws=Sum('draws'), points=Sum('points')
                                    ).order_by('wins', 'draws', 'points').reverse()
        

        return render(request, self.template_name, {'list':matches_or_ranking_list, 'teams_list': set(teams_list)})

class Ranking(TemplateView):
    def get(self, request):
        teams_list = teams()
        ranking_list = TeamsInfo.objects.filter(date = int(timezone.now().year)).values('team_name').annotate(
                                wins=Sum('wins'), losses=Sum('losses'), 
                                draws=Sum('draws'), points=Sum('points')
                                ).order_by('wins', 'draws', 'points').reverse()
        return render(request, self.template_name, {'list':ranking_list, 'teams_list': set(teams_list)})
        