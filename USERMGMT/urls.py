#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
# from django.views.decorators.csrf import csrf_exempt 
# import views
from USERMGMT.views import *

urlpatterns = [
    url(r'error/$', error, name='error'),
    url(r'login/$', connect, name='connect'),
    url(r'logout/$', killUser, name='killUser'),
    url(r'^inscription/$', inscription, name="inscription"),
    url(r'^payment_choice/$', payment_choice, name="payment_choice"),
    url(r'^payment/(?P<amount>.+)/$', payment, name="payment"),
    url(r'^automatic_query/$', automatic_query, name="automatic_query"),
    url(r'^list_profiles/$', list_profiles, name="list_profiles"),
]