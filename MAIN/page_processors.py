#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from MAIN.models import *
from mezzanine.pages.page_processors import processor_for
# from mezzanine.core.request import current_request

@processor_for('/')
def processor_home(request, page):
    Events = Event.objects.all()[:2]
    Associates = Associate.objects.all()[:6]
    RIAs = RIA.objects.all()
    Sponsors = Sponsor.objects.all()
    return locals()

@processor_for(Event)
def processor_event(request, page):
    page = Event.objects.get(pk=page.pk)
    print page
    return locals()
