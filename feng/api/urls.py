__author__ = 'quxl'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from utils.piston_resource import PistonResource as Resource

from handlers import OrderHandler,OrderAcceptHandler

login = login_required(login_url='/api/accounts/login/')

OrderHandler        = Resource(OrderHandler)
OrderAcceptHandler  = Resource(OrderAcceptHandler)
urlpatterns = patterns('',
                       url('^orders/$',login(OrderHandler),name="create_order"),
                       url('^orders/(?P<order_id>\d+)/accept/$',login(OrderAcceptHandler),name="create_order"),
)