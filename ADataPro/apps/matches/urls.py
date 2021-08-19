from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('',  Index.as_view(template_name="matches/list.html"), name = 'index'),
    path('all_matches/<str:id>/',  RankingOrAllMatches.as_view(template_name="matches/list.html"), name = 'all_matches'),
    path('ranking/<str:id>/',  RankingOrAllMatches.as_view(template_name="matches/ranking.html"), name = 'ranking'),
    path('ranking/',  Ranking.as_view(template_name="matches/ranking.html"), name = 'ranking'),
    path('<str:id>/', Search.as_view(template_name="matches/list.html"), name = 'search'),
    path('<str:team_id>/<str:year_id>/',  SearchByYear.as_view(template_name="matches/list.html"), name = 'search_team_by_year'),
]