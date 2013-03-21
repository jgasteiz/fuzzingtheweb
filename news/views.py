import json
import requests

from django.http import HttpResponse
from django.views.generic import View

HACKER_NEWS_API_URL = 'http://api.ihackernews.com/page'


# Not used yet
class HackerNews(View):
    """ Gets the feed of news in news.ycombinator.com """
    def get(self, request, *args, **kwargs):
        r = requests.get(HACKER_NEWS_API_URL)
        # This is doing funny stuff, 500 and more :(
        # json_data = json.dumps(r.json())
        json_data = json.dumps(r.text)
        return HttpResponse(json_data, content_type="application/json")

hacker_news = HackerNews.as_view()


def get_news():
    r = requests.get(HACKER_NEWS_API_URL)
    return json.dumps(r.json())
