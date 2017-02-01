#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from MAIN.models import *
from mezzanine.pages.page_processors import processor_for
# from mezzanine.core.request import current_request

@processor_for('/')
def processor_home(request, page):
    HomeX_data = HomeX.objects.last()
    HomeX_data.inlines = HomeCaption.objects.filter(master=HomeX_data)
    Events = Event.objects.all()[:2]
    for E in Events:
        E.inlines = EventDocumentation.objects.filter(master=E)
    Associates = Associate.objects.all().order_by('-rank')
    RIAs = RIA.objects.exclude(choix_RIA='Assurance professionnelle')
    sponsor_all = Sponsor.objects.all().order_by('?')
    i = 1
    sponsor_list = []
    chunk = []
    for element in sponsor_all:
        if i%6 == 0 or i == len(sponsor_all): 
            chunk.append(element)
            sponsor_list.append(chunk)
            chunk = []
        else: 
            chunk.append(element)
            # print u"#"+str(i)+str(chunk)
        i += 1


    return locals()

@processor_for(Event)
def processor_event(request, page):
    page = Event.objects.get(pk=page.pk)
    print page
    return locals()
