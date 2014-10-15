import datetime
from django.contrib.auth.models import User

__author__ = 'quxl'
from  django import  forms


class RegisterForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        del self.fields['last_login']
        del self.fields['date_joined']

    class Meta:
        model = User

    def clean_last_login(self):
        return datetime.datetime.now()
    def clea_date_joined(self):
        return datetime.datetime.now()