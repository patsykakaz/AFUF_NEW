#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from USERMGMT.forms import LoginForm


def customContextProcessor(request):

    return {
        "navCats": [
                    ("News","/news/"),
                    ("Evènements", "/events"),
                    ("CHU", "/regions/"),
                    ("Comité","/"),
                    ("Remplacements & RCP","/"),
                    ("Partenaires","/")],
        "loginForm": LoginForm()
    }