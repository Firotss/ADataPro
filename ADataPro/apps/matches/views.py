from django.shortcuts import render

from .models import Matches

def index(request):
    matches_list = Matches.objects.all()
    return render(request, 'matches/list.html', {'matches_list': matches_list})