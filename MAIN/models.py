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



class HomeX(Page):
    partenaire_caption = RichTextField(help_text='Chapeau page Partenaires', null=False, blank=True)
    ria_caption = RichTextField(help_text='Chapeau page R.I.A.', null=False, blank=True)
class HomeCaption(models.Model):
    master = models.ForeignKey("HomeX")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("MAIN.HomeX", "HomeX"),
        format="Image", max_length=255, help_text='Dimensions souhaitées : 2400px par 800px')
    lien = models.CharField(max_length=255, null=True, blank=True, help_text='Lien vers lequel dirige l\'image en question')
    external = models.BooleanField(default=False, verbose_name='Externe ?')

    class Meta:
        verbose_name = 'Carousel'

class Event(Page, RichText):
    illustration = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.Event.illustration", "Event"),
        format="Image", max_length=255, null=True, blank=False)
    sponsor_event = models.ForeignKey("Sponsor", null=True, blank=True)
    location = models.CharField(max_length=255, verbose_name='Lieu de l\'évènement', null=True, blank=True)
    pinpoint = models.URLField(verbose_name='Lien externe pour localiser l\'évènement (google maps...)', null=True, blank=True)
    link_event = models.URLField(verbose_name='Lien vers le site évènement', null=True, blank=True)
    date_event = models.DateField(verbose_name='Date évènement', null=True, blank=False)
    time_event = models.CharField(max_length=255, verbose_name='Horaires évènement', null=True, blank=False)
    # subscription_limit = models.CharField(max_length=255, verbose_name='Date limite d\'inscription', blank=True)
    contact =  models.EmailField(max_length=255, verbose_name='contact évènement')
    # documentation = models.FileField(verbose_name='Doc évènement',upload_to='uploads/events/', blank=True, help_text='Documentation disponible au téléchargement pour les utilisateurs loggés')

    class Meta:
        verbose_name = 'EVENEMENT'
        verbose_name_plural = 'EVENEMENTS'

    def save(self, *args, **kwargs):
        try: 
            parent = Page.objects.get(title="EVENEMENTS")
            self.parent = parent
        except:
            pass
        super(Event, self).save(*args, **kwargs)

class EventDocumentation(models.Model):
    master = models.ForeignKey("Event")
    file =  models.FileField(verbose_name='Doc évènement',upload_to='uploads/events/', blank=True, help_text='Documentation disponible au téléchargement pour les utilisateurs loggés')
    nature = models.CharField(max_length=255, verbose_name='Nature document')
    class Meta:
        verbose_name = 'Documentation'

class CHU(Page):
    region_choices = (
        ('Est', 'Est'),
        ('Nord', 'Nord'),
        ('Ouest', 'Ouest'),
        ('Rhône-Alpes', 'Rhône-Alpes'),
        ('Sud', 'Sud'),
        ('Sud-Ouest', 'Sud-Ouest'),
        ('DOM-TOM', 'DOM-TOM'),
        ('Ile de France','Ile de France'),
    )
    region = models.CharField(max_length=255,choices=region_choices,null=False,blank=False,verbose_name='Région du CHU')
    region_description = RichTextField(verbose_name='Description de la région')
    CHU_description = RichTextField(verbose_name='Description du CHU')
    nb_postes = models.CharField(max_length=255, null=False, blank=True,verbose_name='Nombre de postes')
    nb_internes = models.CharField(max_length=255, null=False, blank=True,verbose_name='Nombre d\'internes')
    nb_services = models.CharField(max_length=255, null=False, blank=True,verbose_name='Nombre de services')
    nb_PUPH = models.CharField(max_length=255, null=False, blank=True,verbose_name='Nombre de PUPH')
    robotics = models.BooleanField(verbose_name='Chirurgie robotique')
    thematiques = models.CharField(max_length=255, verbose_name='Thématiques spécifiques')
    referent_AFUF = models.ForeignKey("Associate")
    chef_service = models.CharField(max_length=255, verbose_name='Chef de service')
    coordinateur = models.CharField(max_length=255, verbose_name='Coordinateur')

    class Meta:
        verbose_name = 'C.H.U'
        verbose_name_plural = 'C.H.U'

    def save(self, *args, **kwargs):
        try: 
            parent = Page.objects.get(title="CHU")
            self.parent = parent
        except:
            pass
        super(CHU, self).save(*args, **kwargs)

class Associate(Page, RichText):
    rank = models.IntegerField(default=0,verbose_name='Rang',help_text='Plus le nombre est grand, plus la personne arrivera en tete.')
    prenom = models.CharField(max_length=255, blank=False, verbose_name='Prénom',)
    photo = FileField(verbose_name=_("Photo"),
        upload_to=upload_to("MAIN.Associate.photo", "photo"),
        format="Image", max_length=255, null=False, blank=False)
    statut = models.CharField(max_length=255, blank=False, verbose_name='Statut',)
    ville_exercice = models.CharField(max_length=255, blank=False, verbose_name='Ville d\'exercice')
    email = models.EmailField(null=False, blank=False)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    # search_fields = ('title')

    class Meta:
        verbose_name = 'MEMBRE AFUF'
        verbose_name_plural = 'MEMBRES AFUF'

    def save(self, *args, **kwargs):
        try: 
            parent = Page.objects.get(title="ADMINISTRATION")
            self.parent = parent
        except:
            pass
        super(Associate, self).save(*args, **kwargs)

class Sponsor(Page, RichText):
    logo = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.Event.logo_sponsor", "Sponsor"),
        format="Image", max_length=255, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    label_choices = (
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
    )
    label = models.CharField(max_length=255,choices=label_choices,default=None,)

    class Meta:
        verbose_name = 'SPONSOR'
        verbose_name_plural = 'SPONSORS'

    def save(self, *args, **kwargs):
        try: 
            parent = Page.objects.get(title="PARTENAIRES")
            self.parent = parent
        except:
            pass
        super(Sponsor, self).save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        try: 
            parent = Page.objects.get(title="RIA")
            self.parent = parent
        except:
            pass
        super(RIA, self).save(*args, **kwargs)
