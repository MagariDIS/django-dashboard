from requests_oauthlib import OAuth1Session
import time, calendar
import datetime
import json
import re
import os
import requests
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post, Tmodel

def list_books(request):
    return HttpResponse("Hello world!")


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'template/timeline.html', {})

def index(request):

    msg = request.GET.get('words')

    # magarirobo-node01 API Key
    C_KEY = 'oMeeKukHGY5hJ9Rrwd6B2EI7n'
    C_SECRET = '49MOg3rg57IitjFeTQhKYRrUPUCiAjxmUAknVkDFbfjoKdfyHZ'
    A_KEY = '1167322702534729729-1gI9EQolQHe2By6WqndeOVbacr8ybb'
    A_SECRET = 'vUrexAdJdKJH23e2RuIn5NZPCeqU02pQPB4YlAA608vEH'

    url = 'https://api.twitter.com/1.1/statuses/update.json'
    params = {'status': msg,'lang': 'ja'}
    tw = OAuth1Session(C_KEY,C_SECRET,A_KEY,A_SECRET)
    req = tw.post(url, params = params)


    url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
    params = {'count': 1}
    req = tw.get(url, params = params)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        limit = req.headers['x-rate-limit-remaining']

        for tweet in timeline:
            Text = (tweet['text'])
            User = (tweet['user']['screen_name'])
            Name = (tweet['user']['name'])
            Img = (tweet['user']['profile_image_url'])
            Created_at = YmdHMS(tweet['created_at'])

            data = Tmodel()
            data.user_id = User
            data.user_name = Name
            data.user_img = Img
            data.user_text = Text
            data.user_created_at = Created_at
            data.save()

            Message = {
                'Words': msg,
                'timeline': timeline,
                'API_limit': limit,
                'Text': Text,
                'User': User,
                'Name': Name,
                'Img': Img,
                'Created_at': Created_at,
            }

            return render(request, 'index.html', Message)

    else:
        Error = {
            'Error_message': 'API制限中',
        }
        return render(request, 'index.html', Error)


def search(request):

    search_words = 'hogehoge'
    search_words = request.GET.get('words')

    # magarirobo-node01 API Key
    C_KEY = 'oMeeKukHGY5hJ9Rrwd6B2EI7n'
    C_SECRET = '49MOg3rg57IitjFeTQhKYRrUPUCiAjxmUAknVkDFbfjoKdfyHZ'
    A_KEY = '1167322702534729729-1gI9EQolQHe2By6WqndeOVbacr8ybb'
    A_SECRET = 'vUrexAdJdKJH23e2RuIn5NZPCeqU02pQPB4YlAA608vEH'
    tw = OAuth1Session(C_KEY,C_SECRET,A_KEY,A_SECRET)

    url = 'https://api.twitter.com/1.1/search/tweets.json?'
    params = {
                'q': (search_words, 'utf-8'),
                'lang': 'ja',
                'count': '1'
                }
    req = tw.get(url, params = params)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        limit = req.headers['x-rate-limit-remaining']

        for tweet in timeline['statuses']:
            Text = (tweet['text'])
            User = (tweet['user']['screen_name'])
            Name = (tweet['user']['name'])
            Img = (tweet['user']['profile_image_url'])
            Created_at = YmdHMS(tweet['created_at'])


            data = Supermodel()
            data.user_id = User
            data.user_name = Name
            data.user_img = Img
            data.user_text = Text
            data.user_created_at = Created_at
            data.save()

            Message = {
                'Words': search_words,
                'timeline': timeline,
                'API_limit': limit,
                'Text': Text,
                'User': User,
                'Name': Name,
                'Img': Img,
                'Created_at': Created_at,
            }

            return render(request, 'search.html', Message)

    else:
        Error = {
            'Error_message': 'API制限中',
        }
        return render(request, 'search.html', Error)


def mentions(request):

    msg = request.GET.get('words')

    # magarirobo-node01 API Key
    C_KEY = 'oMeeKukHGY5hJ9Rrwd6B2EI7n'
    C_SECRET = '49MOg3rg57IitjFeTQhKYRrUPUCiAjxmUAknVkDFbfjoKdfyHZ'
    A_KEY = '1167322702534729729-1gI9EQolQHe2By6WqndeOVbacr8ybb'
    A_SECRET = 'vUrexAdJdKJH23e2RuIn5NZPCeqU02pQPB4YlAA608vEH'

    url = 'https://api.twitter.com/1.1/statuses/update.json'
    params = {'status': msg,'lang': 'ja'}
    tw = OAuth1Session(C_KEY,C_SECRET,A_KEY,A_SECRET)
    req = tw.post(url, params = params)


    url = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
    params = {'count': 1}
    req = tw.get(url, params = params)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        limit = req.headers['x-rate-limit-remaining']

        for tweet in timeline:
            Text = (tweet['text'])
            User = (tweet['user']['screen_name'])
            Name = (tweet['user']['name'])
            Img = (tweet['user']['profile_image_url'])
            Created_at = YmdHMS(tweet['created_at'])

            Message = {
                'Words': msg,
                'timeline': timeline,
                'API_limit': limit,
                'Text': Text,
                'User': User,
                'Name': Name,
                'Img': Img,
                'Created_at': Created_at,
            }

            return render(request, 'mentions.html', Message)

    else:
        Error = {
            'Error_message': 'API制限中',
        }
        return render(request, 'mentions.html', Error)


def YmdHMS(created_at):
    time_utc = time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
    unix_time = calendar.timegm(time_utc)
    time_local = time.localtime(unix_time)
    return int(time.strftime('%Y%m%d%H%M%S', time_local))
