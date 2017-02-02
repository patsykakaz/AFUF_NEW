#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from USERMGMT.forms import LoginForm
from MAIN.models import HomeX


def customContextProcessor(request):

    return {
        "navCats": [
                    ("News","/news/"),
                    ("Evènements", "/events/"),
                    ("CHU", "/regions/"),
                    # ("Comité","/"),
                    ("Remplacements & RCP","/ria/"),
                    ("Partenaires","/partenaires/")],
        "loginForm": LoginForm(),
        "HomeX": HomeX.objects.last()
    }