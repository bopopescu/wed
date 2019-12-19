from django.contrib.auth.hashers import check_password, make_password
from home.models import UserModel as User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse


class SettingsBackend:
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:


    ADMIN_PASSWORD = 'pbkdf2_sha256'
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            user = None
        if user is not None:
            try:
                assert check_password(password, user.password) is not False, Exception('密码错误')

                request.session['username'] = username
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = None
            except Exception as e:
                print(e)
                user = None
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    @staticmethod
    def username(username: str):
        try:
            res = User.objects.filter(username__exact=username).first()
        except Exception as e:
            res = None
        return res


def require_login_user(function=None, login_url=None):
    def func(request):
        print(request.user)
        if request.user is None:
            return HttpResponseRedirect(reverse('show.login') if login_url is None else login_url)
        return function(request)

    return func