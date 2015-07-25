from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.defaults import page_not_found

# Decorator to use built-in authentication system                                                                                                                         
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
# Used to create and manually log in a user                                                                                                                              \
                                                                                                                                                                          
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate

# Django transaction system so we can use @transaction.atomic                                                                                                            \
                                                                                                                                                                          
from django.core.urlresolvers import reverse
from django.db import transaction
import json
from datetime import datetime
from time import mktime
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from datetime import datetime
from UQ.models import *


def home(request ):
    context = {}
    context['videoUrl'] = "https://www.youtube.com/embed/lp-EO5I60KA?autoplay=true"
    group = Group(group_name="group1", group_pw="password")
    group.save()
    return render(request, 'UQ/home.html', context)
    
def playLink(request):
    context = {}
    url = request.POST['link']
    url = url.replace('watch?v=','embed/')
    url = url + "?autoplay=true"
    context['videoUrl'] = url

    group = Group.objects.get(group_name="group1")
    song = Song(song_name="default", song_url=url, song_score=0, song_group=group)
    song.save()

    print Song.objects.all()
    return render(request, 'UQ/home.html', context)

def upVote(request):
    song_id = request.GET['id']
    song = Song.objects.get(id=song_id)
    song.song_score = song.song_score + 1
    song.save()

def downVote(request):
    song_id = request.GET['id']
    song = Song.objects.get(id=song_id)
    song.song_score = song.song_score - 1
    song.save()
