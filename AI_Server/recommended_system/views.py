# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import json
import recommendation

def index(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is the polls app")
    return response

def getmusic(request):
    # json_data = '{"hello": "world", "foo": "bar"}'
    # data = recommendation.get_product()
    # return JsonResponse(data)
    # day = request.GET['day']
    # hour = request.GET['hour']
    music = recommendation.get_music()
    return JsonResponse(music, safe=False)