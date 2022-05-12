import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import Game2048

# Create your views here.

# test_user
# 8!S#5RP!WVMACg


def game(request):

    return render(request, 'game_2048/index.html')


def set_result(request):
    user = request.user if str(
        request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    if request.method == 'POST':
        # Get the game state from the POST request
        game_state = request.body

        obj = Game2048.objects.get(user=user)

        # Check if the game state idendical to the server game state
        if game_state != obj.game_state:
            # let string to JSON object
            json_game_state = json.loads(game_state)
            # extract value of best from JSON objest
            obj.best_score = json_game_state['best']
            obj.game_state = json_game_state  # save JSON object to game_state
            obj.save()
    else:
        return redirect('game_2048:game')

    return JsonResponse("", safe=False)


def get_result(request):
    # Check if user is logged in if not set user to test_user
    user = request.user if str(
        request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    if request.method == 'GET':
        obj, created = Game2048.objects.get_or_create(user=user)
        game_state = obj.game_state

    return JsonResponse(game_state, safe=False)
