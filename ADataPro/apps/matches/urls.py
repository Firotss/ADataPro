from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('next_matches/', views.weekend_matches, name = 'next_matches'),
    path('all_matches/<str:id>/', views.all_matches, name = 'all_matches'),
    path('ranking/<str:id>/', views.ranking, name = 'ranking'),
    path('<str:id>/', views.search, name = 'search'),
]