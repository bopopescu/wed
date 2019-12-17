from home.models import *
from django.contrib.auth.hashers import make_password
from django.conf import settings
import time


class UserClass:

    @staticmethod
    def create(**kwargs):
        data: dict = {}
        data['username'] = kwargs.get('username'),
        data['password'] = make_password(kwargs.get('password', '123456'), None, settings.ENCODE_MODE)
        data['create_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        data['update_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        return UserModel.create(**data)

    @staticmethod
    def update(id, data: dict):
        try:
            res = UserModel.objects.filter(id=id).update(**data)
        except UserModel.DoesNotExist:
            res = None
        return res

    @staticmethod
    def select():
        return UserModel.objects.all()

    @staticmethod
    def delete(id):
        user = UserModel.objects.get(pk=id)
        return user.delete()
