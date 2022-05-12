import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import GameTrex

# Create your views here.

def game(request):

    return render(request, "game_trex/index.html")


def set_result(request):
    user = request.user if str(
        request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    if request.method == 'POST':
        
        list_result = json.loads(request.body)

        # distance run store in end of list
        distance_run = list_result.pop(-1)

        # delete unused data
        del list_result[:3]

        # concatinate list to string
        best_score = ''.join(list_result)

        obj = GameTrex.objects.get(user=user)

        if distance_run > obj.best_distance:
            obj.best_score = int(best_score)
            obj.best_distance = distance_run
            obj.save()
    else:
        return redirect('game_trex:game')

    return JsonResponse("", safe=False)


def get_result(request):
    user = request.user if str(
        request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    if request.method == 'GET':
        obj = GameTrex.objects.get(user=user)
        return JsonResponse({'score': obj.best_distance})
