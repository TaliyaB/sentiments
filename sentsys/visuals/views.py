from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello world!")

def upload(request):
    template = loader.get_template('up.html')
    return HttpResponse(template.render())

def visuals(request):
    template = loader.get_template('visuals.html')
    return HttpResponse(template.render())

def data(request):
    template = loader.get_template('data.html')
    return HttpResponse(template.render())

def lda(request):
    template = loader.get_template('LDA.html')
    return HttpResponse(template.render())

