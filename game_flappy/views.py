import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import GameFlappy


def flappy(request):

    return render(request, 'game_flappy/index.html')


def set_result(request):
    user = request.user if str(
        request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    if request.method == 'POST':
        score = json.loads(request.body)
        obj = GameFlappy.objects.get(user=user)

        if score > obj.best_score:
            obj.best_score = score
            obj.save()
    else:
        return redirect('game_flappy:flappy')

    return JsonResponse("", safe=False)


def get_result(request):
    # Check if user is logged in if not set user to test_user
    user = request.user if str(
        request.user) != "AnonymousUser" else User.objects.get(username='test_user')

    if request.method == 'GET':
        obj, created = GameFlappy.objects.get_or_create(user=user)
        return JsonResponse({'score': obj.best_score})
