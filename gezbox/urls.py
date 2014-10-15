from django.conf.urls import patterns, include, url
from django.contrib.auth import admin
from django.views.generic.base import TemplateView



urlpatterns = patterns('',
                       url(r'^$',TemplateView.as_view(template_name='home.html'), name='home'),
                       url(r'^api/feng/',include('feng.api.urls')),
                       url(r'^api/accounts/',include('accounts.api.urls')),
)