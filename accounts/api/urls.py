__author__ = 'quxl'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from utils.piston_resource import PistonResource as Resource

from handlers import LoginHandler,LogOutHandler,RegisterHandler

LoginHandler    = Resource(LoginHandler)
LogOutHandler   = Resource(LogOutHandler)
RegisterHandler = Resource(RegisterHandler)
urlpatterns = patterns('',
                       url(r'^login/$',LoginHandler,name="login"),
                       url(r'^login/$',LoginHandler,name="login"),
                       url(r'^reg/$',RegisterHandler,name="reg"),
)