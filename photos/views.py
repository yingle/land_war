from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    template = loader.get_template('photos/index.html')
    return HttpResponse(template.render())


def winningest(request):
    return HttpResponse("You are at the winningest photo.")


def losingest(request):
    return HttpResponse("You are at the losingest photo.")

@login_required(login_url='login/')
def add_photo(request):
    form = UploadImageForm()
    return render(request, 'photos/add.html', {'form':form,})


