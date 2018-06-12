# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from dwebsocket.decorators import require_websocket
from django.http import HttpResponse
import subprocess


# Create your views here.
def index(request):
    return render(request, 'index.html')


@require_websocket
def update(request):
    for i in request.websocket:
        p = subprocess.Popen('%s' % (i), shell=True, stdout=subprocess.PIPE)
        for line in iter(p.stdout.readline, b''):
            request.websocket.send(str(line.rstrip()))
