from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.


def index(request):
    template = loader.get_template('photos/index.html')
    return HttpResponse(template.render())


def winningest(request):
    return HttpResponse("You are at the winningest photo.")


def losingest(request):
    return HttpResponse("You are at the losingest photo.")

