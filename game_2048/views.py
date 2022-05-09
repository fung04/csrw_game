from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import Game2048
from django.contrib.auth.models import User

# Create your views here.

#test_user
#8!S#5RP!WVMACg


def game(request):

    # Check if user is logged in
    user = request.user if str(request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    obj, created = Game2048.objects.get_or_create(user=user)

    return render(request, 'game_2048/index.html')


def set_result(request):
    user = request.user if str(request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    if request.method == 'POST':
        # Get the game state from the POST request
        game_state = request.body

        obj = Game2048.objects.get(user=user)
        if game_state != obj.game_state:
            json_game_state = json.loads(game_state)  # let string to JSON object
            obj.best_score = json_game_state['best']  # extract value of best from JSON objest
            obj.game_state = json_game_state  # save JSON object to game_state
            obj.save()
    else:
        return redirect('game_2048:game')

    return JsonResponse("", safe=False)


def get_result(request):
    user = request.user if str(request.user) != "AnonymousUser" else User.objects.get(username='test_user')
    
    obj, created = Game2048.objects.get_or_create(user=user)

    game_state = obj.game_state

    return JsonResponse(game_state, safe=False)
