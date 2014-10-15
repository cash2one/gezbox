import logging
import traceback
import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from piston.handler import BaseHandler
from django.contrib.auth import login as auth_login, logout as auth_logout
from piston.utils import FormValidationError, rc
from accounts.api.forms import RegisterForm
from feng.models import Account

log = logging.getLogger("root")
__author__ = 'quxl'

class LoginHandler(BaseHandler):
    allowed_methods = ['POST']

    def create(self, request, *args, **kwargs):
        log.debug(request)
        f = AuthenticationForm(data=request.POST)
        if f.is_valid():
            log.debug("f.is_valid()")
            auth_login(request,f.get_user())
        else:
            log.debug("FormValidationError")
            raise FormValidationError(f)
        request.META['slogin']=True
        return request.user


class LogOutHandler(BaseHandler):
    allowed_methods = ["GET"]

    def read(self, request, *args, **kwargs):
        auth_logout(request)
        return rc.ALL_OK


class RegisterHandler(BaseHandler):
    allowed_methods = ["POST"]

    def create(self, request, *args, **kwargs):
        f = RegisterForm(request.POST)
        if f.is_valid():
            username = f.cleaned_data['username']
            password = f.cleaned_data['password']
            inst = User.objects.create_user(username,'',password)
            account = Account(balance=0,master = inst)
            account.save()
            return inst
        else:
            raise FormValidationError(f)


