from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import GameTrex
from django.contrib.auth.models import User
import json


# Create your views here.

def game(request):
    user = request.user if str(request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    obj, created = GameTrex.objects.get_or_create(user=user)

    return render(request, "game_trex/index.html", {'result': obj})


def get_score(request):
    user = request.user if str(request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    if request.method == 'POST':
        array_result = json.loads(request.body)  # convert decode result to array

        distance = array_result.pop(-1)  # distance run store in last list
        del array_result[:3]  # delete useless data in array

        result = str()  # init result as string
        for i in array_result:
            result += str(i)  # concatenate best result

        obj = GameTrex.objects.get(user=user)

        if distance > obj.best_distance:
            obj.best_score = int(result)
            obj.best_distance = distance
            obj.save()
    else:
        return redirect('game_trex:game')

    return JsonResponse("", safe=False)
