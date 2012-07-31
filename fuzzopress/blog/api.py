# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from fuzzopress.blog.models import Post

def entries(request):
    posts_qs = Post.objects.published()
    array_posts = []
    for p in posts_qs:
        array_posts.append({'title': p.title, 'body': p.body})
    return HttpResponse(json.dumps(array_posts), mimetype="application/json")