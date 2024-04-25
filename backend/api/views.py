from django.shortcuts import render
from django.http import JsonResponse


def button_view(request):
    return JsonResponse({'message': 'Hello World'})
