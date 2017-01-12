#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin

from mezzanine.pages.admin import PageAdmin
from MAIN.models import *

Event_fieldsets = deepcopy(PageAdmin.fieldsets)
Event_fieldsets[0][1]["fields"].insert(-1, "illustration")
Event_fieldsets[0][1]["fields"].insert(-1, "sponsor_event")
Event_fieldsets[0][1]["fields"].insert(-1, "location")
Event_fieldsets[0][1]["fields"].insert(-1, "pinpoint")
Event_fieldsets[0][1]["fields"].insert(-1, "link_event")
Event_fieldsets[0][1]["fields"].insert(-1, "date_event")
Event_fieldsets[0][1]["fields"].insert(-1, "time_event")
Event_fieldsets[0][1]["fields"].insert(-1, "subscription_limit")
Event_fieldsets[0][1]["fields"].insert(-1, "contact")
Event_fieldsets[0][1]["fields"].insert(-1, "documentation")
Event_fieldsets[0][1]["fields"].insert(-1, "content")
class EventAdmin(PageAdmin):
    fieldsets = Event_fieldsets

    # def has_module_permission(self, request):
        # return True

CHU_fieldsets = deepcopy(PageAdmin.fieldsets)
CHU_fieldsets[0][1]["fields"].insert(-1, "region")
CHU_fieldsets[0][1]["fields"].insert(-1, "region_description")
CHU_fieldsets[0][1]["fields"].insert(-1, "CHU_description")
CHU_fieldsets[0][1]["fields"].insert(-1, "nb_postes")
CHU_fieldsets[0][1]["fields"].insert(-1, "nb_internes")
CHU_fieldsets[0][1]["fields"].insert(-1, "nb_services")
CHU_fieldsets[0][1]["fields"].insert(-1, "nb_PUPH")
CHU_fieldsets[0][1]["fields"].insert(-1, "robotics")
CHU_fieldsets[0][1]["fields"].insert(-1, "thematiques")
CHU_fieldsets[0][1]["fields"].insert(-1, "referent_AFUF")
CHU_fieldsets[0][1]["fields"].insert(-1, "chef_service")
CHU_fieldsets[0][1]["fields"].insert(-1, "coordinateur")
class CHUAdmin(PageAdmin):
    fieldsets = CHU_fieldsets

    # def has_module_permission(self, request):
        # return True

Associate_fieldsets = deepcopy(PageAdmin.fieldsets)
Associate_fieldsets[0][1]["fields"].insert(-1, "prenom")
Associate_fieldsets[0][1]["fields"].insert(-1, "statut")
Associate_fieldsets[0][1]["fields"].insert(-1, "ville_exercice")
Associate_fieldsets[0][1]["fields"].insert(-1, "content")
Associate_fieldsets[0][1]["fields"].insert(-1, "facebook")
Associate_fieldsets[0][1]["fields"].insert(-1, "linkedin")
Associate_fieldsets[0][1]["fields"].insert(-1, "twitter")
class AssociateAdmin(PageAdmin):
    fieldsets = Associate_fieldsets

    # def has_module_permission(self, request):
        # return True

RIA_fieldsets = deepcopy(PageAdmin.fieldsets)
RIA_fieldsets[0][1]["fields"].insert(-1, "choix_RIA")
RIA_fieldsets[0][1]["fields"].insert(-1, "logo_sponsor")
RIA_fieldsets[0][1]["fields"].insert(-1, "target_link")
RIA_fieldsets[0][1]["fields"].insert(-1, "mail")
RIA_fieldsets[0][1]["fields"].insert(-1, "illustration")
RIA_fieldsets[0][1]["fields"].insert(-1, "content")
class RIAAdmin(PageAdmin):
    fieldsets = RIA_fieldsets

    # def has_module_permission(self, request):
        # return True


Sponsor_fieldsets = deepcopy(PageAdmin.fieldsets)
Sponsor_fieldsets[0][1]["fields"].insert(-1, "label")
Sponsor_fieldsets[0][1]["fields"].insert(-1, "logo")
Sponsor_fieldsets[0][1]["fields"].insert(-1, "website")
Sponsor_fieldsets[0][1]["fields"].insert(-1, "content")
class SponsorAdmin(PageAdmin):
    fieldsets = Sponsor_fieldsets

    # def has_module_permission(self, request):
        # return True

admin.site.register(Event, EventAdmin)
admin.site.register(CHU, CHUAdmin)
admin.site.register(Associate, AssociateAdmin)
admin.site.register(RIA, RIAAdmin)
admin.site.register(Sponsor, SponsorAdmin)






