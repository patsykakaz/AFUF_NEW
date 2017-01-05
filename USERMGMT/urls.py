#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
# from django.views.decorators.csrf import csrf_exempt 
# import views
from USERMGMT.views import *

urlpatterns = [
    url(r'^inscription/$', inscription, name="inscription"),
    url(r'^payment/$', payment, name="payment"),
    url(r'^automatic_query/$', automatic_query, name="automatic_query"),
]