from django.shortcuts import render
from .models import ShowItem
from game_flappy.models import FlappyScore
from game_trex.models import GameTrex
from game_2048.models import Game2048

# Create your views here.


def homepage(request):
    obj = ShowItem.objects.get()

    if obj.video:
        return render(request, 'homepage/index.html', {'obj': obj})
    else:
        return render(request, 'homepage/index.html')


def score(request):

    game_flappy = FlappyScore.objects.order_by('-score')
    game_tiles = GameTrex.objects.order_by('-best_score')
    game_rex = Game2048.objects.order_by('-best_score')

    print(game_flappy)

    context = {
        'flappy': game_flappy,
        'tiles': game_tiles,
        'rex': game_rex,
    }

    return render(request, 'homepage/score_board.html', context)
