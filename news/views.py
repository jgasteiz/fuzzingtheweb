import json
import requests

from django.http import HttpResponse

from .models import NewsFeed

HACKER_NEWS_API_URL = 'http://api.ihackernews.com/page'


def get_news(request=None):
    feed = NewsFeed.objects.latest()
    print json.dumps(feed.json)
    return json.dumps(feed.json)


# View for updating the feed
def update_feed(request):
    r = requests.get(HACKER_NEWS_API_URL)
    feed = NewsFeed()
    feed.json = r.text
    feed.save()
    return HttpResponse(feed.created)
