from django.shortcuts import render, redirect
from django.http import JsonResponse
import base64
import json
from .models import Game2048
from django.contrib.auth.models import User

# Create your views here.

#test_user
#8!S#5RP!WVMACg


def game(request):
    user = request.user if str(request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    obj, created = Game2048.objects.get_or_create(user=user)

    state = str(
        base64.b64encode(
            obj.game_state.encode("utf-8")
        ).decode("utf8")
    )

    return render(request, 'game_2048/index.html', {'obj': obj, 'data': state})


def set_score(request):
    user = request.user if str(request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    if request.method == 'POST':

        game_state = str(
            base64.b64decode(
                request.body
            ).decode("utf-8"))

        obj = Game2048.objects.get(user=user)
        if game_state != obj.game_state:
            json_read_best = json.loads(game_state)  # let string to JSON object
            obj.best_scores = json_read_best['best']  # extract value of best from JSON objest
            obj.game_state = game_state
            obj.save()
    else:
        return redirect('game_2048:game')

    return JsonResponse("", safe=False)
