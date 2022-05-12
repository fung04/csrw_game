from django.shortcuts import render

from game_2048.models import Game2048
from game_flappy.models import GameFlappy
from game_trex.models import GameTrex

from .models import ShowItem

# Create your views here.


def homepage(request):
    obj = ShowItem.objects.get()

    if obj.video:
        return render(request, 'homepage/index.html', {'obj': obj})
    else:
        return render(request, 'homepage/index.html')


def score(request):

    game_flappy = GameFlappy.objects.order_by('-best_score')
    game_tiles = Game2048.objects.order_by('-best_score')
    game_rex = GameTrex.objects.order_by('-best_score')


    context = {
        'flappy': game_flappy,
        'tiles': game_tiles,
        'rex': game_rex,
    }

    return render(request, 'homepage/score_board.html', context)
