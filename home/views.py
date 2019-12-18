from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from logic.mybackend import SettingsBackend
import json
from home.logic import UserClass
from django.urls import reverse


# Create your views here.


def login(request):
    if request.method == 'POST':
        setting_logic = SettingsBackend()
        data = request.POST
        res = setting_logic.authenticate(request, data['username'], data['password'])
        if res:
            result = {"status": "success", "url": reverse('show.index')}
        else:
            result = {"status": "failure"}
        return JsonResponse(result, content_type="application/json,charset=utf-8")

    return render(request, 'admin/login.html')


def index(request):
    return render(request, 'admin/index.html')


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('show.login'))


def welcome(request):
    return render(request, 'admin/welcome.html')


def create_user(request):
    if request.method == 'POST':
        data = request.POST

        res = UserClass.create(**data)

        status = {"status": "success", "msg": "添加成功", "data": model_to_dict(res)} if res is not None else {"status": "failure", "msg": "用户已经存在", "data": []}

        return HttpResponse(json.dumps(status), content_type="application/json")

