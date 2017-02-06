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

@processor_for('events')
def processor_event(request, page):
    try:
        illustration = HomeCaption.objects.get(lien__contains="events")
        # print "illustration = %s" %illustration
    except:
        pass
    Events = Event.objects.all()
    for E in Events:
        E.inlines = EventDocumentation.objects.filter(master=E)
    return locals()

@processor_for(Event)
def processor_event(request, page):
    page = Event.objects.get(pk=page.pk)
    print page
    return locals()


@processor_for('regions')
def processor_event(request, page):
    try:
        illustration = HomeCaption.objects.get(lien__contains="regions")
        # print "illustration = %s" %illustration
    except:
        pass
    all_CHU = []
    all_region = []
    for region in CHU.region_choices:
        x = [region, CHU.objects.filter(region=region[0])]
        all_CHU.append(x)
        all_region.append(region[0])
    return locals()

@processor_for('ria')
def processor_event(request, page):
    try: 
        illustration = HomeCaption.objects.get(lien__contains="ria")
        # print "illustration = %s" %illustration
    except:
        pass
    Rs = RIA.objects.filter(choix_RIA="Remplacement")
    Is = RIA.objects.filter(choix_RIA="Installation")
    As = RIA.objects.filter(choix_RIA="Assurance professionnelle")
    # RIAs = RIA.objects.all()
    return locals()

@processor_for('partenaires')
def processor_event(request, page):
    try: 
        illustration = HomeCaption.objects.get(lien__contains="partenaires")
        # print "illustration = %s" %illustration
    except:
        pass
    sponsors = Sponsor.objects.all().order_by('label')
    return locals()
