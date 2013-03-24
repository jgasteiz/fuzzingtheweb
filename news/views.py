import json
import requests
from time import sleep

from django.http import HttpResponse

from .models import NewsFeed

HACKER_NEWS_API_URL = 'http://api.ihackernews.com/page'


def get_news(request=None):
    feed = NewsFeed.objects.latest()
    return json.dumps(feed.json)


# View for updating the feed
def update_feed(request):
    feed = NewsFeed()
    feed = get_feed(feed)
    return HttpResponse(feed.created)


# Will document this soon.
def get_feed(feed):
    r = requests.get(HACKER_NEWS_API_URL)
    if r.status_code == 200:
        feed.json = r.text
        feed.save()
    else:
        print "Trying again..."
        sleep(10)
        get_feed(feed)
    return feed


def update_feed_internal():
    feed = NewsFeed()
    feed = get_feed(feed)
    return feed.created
