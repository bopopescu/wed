from django.http import JsonResponse
from django.shortcuts import render, HttpResponse


# Create your views here.


def login(request):
    return JsonResponse({
        "status": "success"
    })