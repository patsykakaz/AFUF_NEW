#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from USERMGMT.forms import LoginForm


def customContextProcessor(request):

    return {
        "navCats": [("Evènements & formations", "/events"),
                    ("Régions & CHU", "/regions/"),
                    ("Le Comité","/"),
                    ("Remplacements & RCP","/"),
                    ("Nos Partenaires","/")],
        "loginForm": LoginForm()
    }