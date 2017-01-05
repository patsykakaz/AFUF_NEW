#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import random, hashlib
from datetime import datetime #, date, time

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib.auth import login , logout, authenticate#, get_backends, get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError

from forms import *

def inscription(request):
    if not request.POST:
        form = NewUserForm()
    else: 
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            passwordBase = request.POST['email']+request.POST['nom']
            hash_object = hashlib.sha256(passwordBase.encode('utf8'))
            password = hash_object.hexdigest()
            password = str(password)[:8]
            print password
            try: 
                k = User.objects.create_user(
                            username=request.POST['prenom'] +'_'+request.POST['nom'],
                            email=request.POST['email'],
                            password=password
                        )
                k.save()
            except IntegrityError as e:
            # username is unique and already exists in DB
                k = User.objects.create_user(
                            username=request.POST['prenom']+'_'+request.POST['nom']+" ["+datetime.now().strftime("%d/%m/%Y - %H:%M")+"]",
                            email=request.POST['email'],
                            password=password
                        )
                k.save()
            newProfile = form.save(commit=False)
            newProfile.user = k
            newProfile.save()
            login(request, k)
            validation = "ALL GOOD"
            return redirect(reverse('payment'))
    return render(request, 'form.html', locals())

# Create your views here.
@login_required
def payment(request):
    print request.POST
    amount = 100
    MERCANET_URL = settings.MERCANET_URL
    # Generate a 6 figure User.pk added to transactionReference to retrieve User after transaction is complete
    emptyList = "000000"
    upk = emptyList[:6-len(str(request.user.profile.pk))] + str(request.user.profile.pk)
    # upk = "888888"
    transactionReference = upk+str(datetime.now().strftime("%d%m%Y%H%M%s"))
    # Building integrity seal
    data = "amount="+str(amount)+"|currencyCode=978|merchantId="+settings.MERCANET_ID+"|normalReturnUrl=http://"+settings.SITE_URL+"/user/automatic_query/|automaticResponseUrl=http://"+settings.SITE_URL+"/user/automatic_query/|transactionReference="+transactionReference+"|keyVersion=1"
    data_to_seal = data+settings.MERCANET_KEY
    hash_object = hashlib.sha256(data_to_seal.encode('utf8'))
    seal = hash_object.hexdigest()
    return render(request, 'payment_false.html', locals())

@csrf_exempt
def automatic_query(request):
    print request
    print "automatic response called", request.POST
    if request.POST and "Data" in request.POST and "Seal" in request.POST:
        data_to_seal = request.POST['Data']+settings.MERCANET_KEY
        hash_object = hashlib.sha256(data_to_seal.encode('utf8'))
        seal = hash_object.hexdigest()
        if request.POST['Seal'] == seal:
            data = request.POST['Data'].split('|')
            for element in data: 
                subElement = element.split('=')
                if subElement[0] == "responseCode":
                    responseCode = subElement[1]
                elif subElement[0] == "transactionReference":
                    pkToUpdate = int(subElement[1][:6])
                    print "pkToUpdate ->", pkToUpdate
                elif subElement[0] == "amount":
                    amount = int(subElement[1])
            if responseCode == "00" and not "manual" in request.path:
                profileToUpdate = Profile.objects.get(pk=pkToUpdate)
                profileToUpdate.choix_adhesion = int(amount)/100
                profileToUpdate.save()
                # send mail to Profile.email
                payment_response = "Success"
                print "transaction successful"
                # try:
                passwordBase = profileToUpdate.email+profileToUpdate.nom
                hash_object = hashlib.sha256(passwordBase.encode('utf8'))
                password = hash_object.hexdigest()
                password = str(password)[:8]
                subject = "Adhésion à l'AFUF"
                from_email = settings.NO_REPLY
                to = profileToUpdate.email
                text_content = u"Bonjour! Nous vous confirmons votre adhésion à l'AFUF pour l'année 2017, et nous vous remercions pour votre confiance! \nPensez à garder précieusement votre login et votre mot de passe qui vont vous être donnés pour pouvoir accéder à toutes les informations du site www.afuf.fr Le comité d'administration de l'AFUF \n login : "+profileToUpdate.email+"\n Mot de passe : "+password
                html_content = u"<p>Bonjour!</p> <p>Nous vous confirmons votre adhésion à l'AFUF pour l'année 2017, et nous vous remercions pour votre confiance!</p><p>pensez à garder précieusement votre login et votre mot de passe qui vont vous être donnés pour pouvoir accéder à toutes les informations du site <a href='www.afuf.fr' target='blank'>afuf.fr</a> <br /> <b>Le comité d'administration de l'AFUF</b></p><p>Login: "+profileToUpdate.email+"</p> <p> mot de passe : "+password+"</p>" 
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                # except:
                #     raise Exception('Erreur email pour user : %s, password : %s' % profileToUpdate.email, password)
            elif responseCode == "00":
                payment_response = "Success"
                print "transaction Success"
            else:
                payment_response = "Fail"
                print "transaction failed"
        else: 
            print "ERROR WITH SEAL"
            raise ValueError('Mercanet SEAL is compromised. FUCK OFF.')
    else:
        return HttpResponse("No Post data sent. You're out of line pal ! ")
    return render(request, 'payment_response.html', locals())