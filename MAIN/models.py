#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext, ugettext_lazy as _

from settings import MEDIA_ROOT
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.utils.models import upload_to

class Event(Page, RichText):
    illustration = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.Event.illustration", "Event"),
        format="Image", max_length=255, null=True, blank=False)
    sponsor_event = models.ForeignKey("Sponsor")
    location = models.CharField(max_length=255, verbose_name='Lieu de l\'évènement')
    pinpoint = models.URLField(verbose_name='Lien externe pour localiser l\'évènement (google maps...)', blank=True)
    date_event = models.DateField(verbose_name='Date évènement', blank=False)
    time_event = models.CharField(max_length=255, verbose_name='Horaires évènement', blank=False)
    subscription_limit = models.CharField(max_length=255, verbose_name='Date limite d\'inscription', blank=False)
    contact =  models.CharField(max_length=255, verbose_name='contact évènement')
    documentation = models.FileField(verbose_name='Doc évènement',upload_to='uploads/events/', blank=True, help_text='Documentation disponible au téléchargement pour les utilisateurs loggés')

    class Meta:
        verbose_name = 'EVENEMENT'
        verbose_name_plural = 'EVENEMENTS'

    # def save(self, *args, **kwargs):
        # print 'saving profile for : ' + self.email
        # super(Profile, self).save(*args, **kwargs)

    # def __str__(self):
        # return '%s %s' % (self.nom, self.prenom)

class CHU(Page):
    region_choices = (
        ('Ile de France','Ile de France'),
        ('Est', 'Est'),
        ('Nord', 'Nord'),
        ('Ouest', 'Ouest'),
        ('Rhône-Alpes', 'Rhône-Alpes'),
        ('Sud', 'Sud'),
        ('Sud-Ouest', 'Sud-Ouest'),
        ('DOM-TOM', 'DOM-TOM'),
    )
    region = models.CharField(max_length=255,choices=region_choices,null=False,blank=False,verbose_name='Région du CHU')
    region_description = RichTextField(verbose_name='Description de la région')
    CHU_description = RichTextField(verbose_name='Description du CHU')
    nb_postes = models.IntegerField(verbose_name='Nombre de postes')
    nb_internes = models.IntegerField(verbose_name='Nombre d\'internes')
    nb_services = models.IntegerField(verbose_name='Nombre de services')
    nb_PUPH = models.IntegerField(verbose_name='Nombre de PUPH')
    robotics = models.BooleanField(verbose_name='Chirurgie robotique')
    thematiques = models.CharField(max_length=255, verbose_name='Thématiques spécifiques')
    referent_AFUF = models.ForeignKey("Associate")
    chef_service = models.CharField(max_length=255, verbose_name='Chef de service')
    coordinateur = models.CharField(max_length=255, verbose_name='Coordinateur')

    class Meta:
        verbose_name = 'C.H.U'
        verbose_name_plural = 'C.H.U'

class Associate(Page, RichText):
    prenom = models.CharField(max_length=255, blank=False, verbose_name='Prénom',)
    photo = FileField(verbose_name=_("Photo"),
        upload_to=upload_to("MAIN.Associate.photo", "photo"),
        format="Image", max_length=255, null=True, blank=False)
    statut = models.CharField(max_length=255, blank=False, verbose_name='Statut',)
    ville_exercice = models.CharField(max_length=255, blank=False, verbose_name='Ville d\'exercice')
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'MEMBRE AFUF'
        verbose_name_plural = 'MEMBRES AFUF'

class Sponsor(Page, RichText):
    logo = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.Event.logo_sponsor", "Event"),
        format="Image", max_length=255, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    label_choices = (
        (None, None),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
    )
    label = models.CharField(max_length=255,choices=label_choices,default=None,)

    class Meta:
        verbose_name = 'SPONSOR'
        verbose_name_plural = 'SPONSORS'

class RIA(Page, RichText):
    RIA_choices = (
        ('Remplacement', 'Remplacement'),
        ('Installation', 'Installation'),
        ('Assurance professionnelle', 'Assurance professionnelle'),
    )
    choix_RIA = models.CharField(max_length=255,choices=RIA_choices,default=None,verbose_name='Remplacement, installation ou Assurance pro ? ')
    logo_sponsor = FileField(verbose_name=_("logo partenaire"),
        upload_to=upload_to("MAIN.RIA.logo", "RIA"),
        format="Image", max_length=255, null=True, blank=True)
    target_link = models.URLField(null=True, blank=True, verbose_name='Lien vers site externe')
    mail = models.EmailField(blank=True, verbose_name='Email contact')
    illustration = FileField(verbose_name=_("Illustration"),
        upload_to=upload_to("MAIN.RIA.illustration", "RIA"),
        format="Image", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'R.I.A'
        verbose_name_plural = 'R.I.A'
