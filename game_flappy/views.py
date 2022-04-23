from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import FlappyScore
from django.contrib.auth.models import User
import json


def flappy(request):
    user = request.user if str(request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    obj, created = FlappyScore.objects.get_or_create(user=user)

    return render(request, 'game_flappy/index.html', {'result': obj})


def set_result(request):
    user = request.user if str(request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    if request.method == 'POST':
        score = json.loads(request.body)
        obj = FlappyScore.objects.get(user=user)

        if score > obj.score:
            obj.score = score
            obj.save()
    else:
        return redirect('game_flappy:flappy')

    return JsonResponse("", safe=False)


def get_result(request):
    user = request.user if str(request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    if request.method == 'GET':
        obj = FlappyScore.objects.get(user=user)
        print(obj.score)
        return JsonResponse({'score': obj.score})

