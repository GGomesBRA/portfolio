from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("projects/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def experiments(request):
    template = loader.get_template("projects/experiments.html")
    context = {}
    return HttpResponse(template.render(context, request))
