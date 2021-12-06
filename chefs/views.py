from django.shortcuts import render
from .models import Team


def team_list(request):
    team_list = Team.objects.all()

    context = {
        'team_list': team_list,
    }

    return render(request, 'chefs/team.html', context)
