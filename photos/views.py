from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import *
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

def index(request):
    template = loader.get_template('photos/index.html')
    return HttpResponse(template.render())


def winningest(request):
    return HttpResponse("You are at the winningest photo.")


def losingest(request):
    return HttpResponse("You are at the losingest photo.")


def all_photos(request):
    current_user = request.user
    all_photo_list = Photo.objects.get(createUser = current_user)
    return render(request,'photos/all_photos.html', {list : all_photo_list})



@login_required()
def add_photo(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.image = form.cleaned_data['image']
            new_photo.kind = form.cleaned_data['kind']
            new_photo.city = form.cleaned_data['city']
            new_photo.description = form.cleaned_data['description']
            new_photo.match_number = 50;
            new_photo.upload_data = datetime.now()
            new_photo.votes = 0
            new_photo.createUser = request.user
            new_photo.save()
            return render_to_response('portal/personal_space.html')
        else:
            return HttpResponseRedirect('/')
    else:
        form = UploadImageForm()
        return render(request, 'photos/add.html', {'form':form,})



