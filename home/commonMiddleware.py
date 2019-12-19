from django.utils.deprecation import MiddlewareMixin

from logic.mybackend import SettingsBackend
from django.http import HttpResponseRedirect
from django.urls import reverse


class AuthUserMiddleware(MiddlewareMixin):

    def process_request(self, request):
        assert hasattr(request, 'session'), ("验证session不存在"
                                             "肯定不在这个地球上"
                                             "please your found he!")
        username = request.session.get('username', None)
        if username:
            request.user = SettingsBackend.username(username)
        else:
            request.user = None


