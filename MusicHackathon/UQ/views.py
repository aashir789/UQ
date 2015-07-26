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
    if (Group.objects.all() == None ):
        group = Group(group_name="group1", group_pw="password")
        group.save()
    group = Group.objects.all()[1]
    
    sortedSongs = Song.objects.order_by('-song_score','song_url')
    context['songs'] = sortedSongs
    return render(request, 'UQ/home.html', context)
    
def playLink(request):
    context = {}
    url = request.POST['link']
    vid = url.rsplit("=")[1]
    context['videoID'] = vid
    group = Group.objects.all()[1]
    song = Song(song_name="default", song_url=url, song_score=0, song_group=group)
    song.save()

    sortedSongs = Song.objects.order_by('-song_score','song_url')
    context['songs'] = sortedSongs
    return redirect(reverse( 'home'))

def upVote(request,id):
    print 'in here'
    print id
    song_id = id
    song = Song.objects.get(id=song_id)
    song.song_score = song.song_score + 1
    print song.song_url
    print song.song_score
    song.save()
    return redirect(reverse('home'))

def downVote(request, id):
    song_id = id
    song = Song.objects.get(id=song_id)
    song.song_score = song.song_score - 1
    print song.song_url
    print song.song_score
    song.save()
    songList = Song.objects.filter(song_group=group)
    sortedSongs = Song.objects.order_by('song_score','song_url') 
    context['songs'] = songList
    return redirect(reverse('home'))


def getVID(request):
    max_score_list = Song.objects.order_by('-song_score', 'song_url')
    bestsong = str(max_score_list[0])
    dick = [{'id':bestsong.rsplit('=')[1]}]
    return HttpResponse(json.dumps(dick),content_type='application/json')



