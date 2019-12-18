from home.models import *
from django.contrib.auth.hashers import make_password
from django.conf import settings
import time


class UserClass:

    data = ['username', 'password', 'status', 'nickname', 'avatar']

    @classmethod
    def create(cls, **kwargs):
        try:
            data = cls().allow_field(kwargs)
            data['create_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            data['update_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            try:
                UserModel.objects.get(username=data['username'])
                res = None
            except UserModel.DoesNotExist:
                res = UserModel.objects.create(**data)
            return res
        except Exception as e:
            print(e)
            return None

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

    def allow_field(self, data: dict):
        result: dict = {}
        for key, field in data.items():
            if key in self.data:
                result[key] = field.pop() if isinstance(field, list) else field
                if key == 'password':
                    result[key] = make_password(result[key], None, settings.ENCODE_MODE)
        return result

    def model(self):
        return UserModel
