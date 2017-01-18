#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from MAIN.models import *
from mezzanine.pages.page_processors import processor_for
# from mezzanine.core.request import current_request

@processor_for('/')
def processor_home(request, page):
    Events = Event.objects.all()[:2]
    Associates = Associate.objects.all()
    RIAs = RIA.objects.all()
    Sponsors = Sponsor.objects.all()
    return locals()
