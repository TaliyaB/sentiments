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


def nouns0(request):
    template = loader.get_template('nouns0.html')
    return HttpResponse(template.render())


def nouns1(request):
    template = loader.get_template('nouns1.html')
    return HttpResponse(template.render())


def nouns2(request):
    template = loader.get_template('nouns2.html')
    return HttpResponse(template.render())


def adj0(request):
    template = loader.get_template('adj0.html')
    return HttpResponse(template.render())


def adj1(request):
    template = loader.get_template('adj1.html')
    return HttpResponse(template.render())


def adj2(request):
    template = loader.get_template('adj2.html')
    return HttpResponse(template.render())


def preprocessed(request):
    template = loader.get_template('preprocessed.html')
    return HttpResponse(template.render())
