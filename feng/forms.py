#encoding:utf-8
import datetime
import logging
import traceback

from django import forms
from feng.models import Order
log = logging.getLogger("root")

__author__ = 'quxl'


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request',None)
        super(OrderForm,self).__init__(*args,**kwargs)

    def clean_master(self):
        log.debug('clean_master')
        try:
            return self.request.user
        except:
            log.error("OrderForm clean_user error %s"%traceback.extract_stack())

    class Meta:
        model = Order
        fields =['descr','price']
