from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from logic.mybackend import SettingsBackend
import json


# Create your views here.


def login(request):
    if request.method == 'POST':
        setting_logic = SettingsBackend()
        data = request.POST
        res = setting_logic.authenticate(request, data['username'], data['password'])
        if res:
            result = {"status": "success"}
        else:
            result = {"status": "failure"}
        return JsonResponse(result, content_type="application/json,charset=utf-8")

    return render(request, 'admin/login.html')


def index(request):
    return render(request, 'admin/index.html')
