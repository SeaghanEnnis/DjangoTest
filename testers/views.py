from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def index(request, *args, **kwargs):
    template = loader.get_template("body.html")
    return HttpResponse(template.render())
