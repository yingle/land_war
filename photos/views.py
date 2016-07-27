from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import *
from django.contrib.auth.decorators import login_required
from datetime import datetime
from models import *
import random
#from django.core.context_processors import csrf


# Create your views here.

def index(request):
    type = random.random()
    if type < 0.33:
        type = 'Beach'
    elif type > 0.66:
        type = 'Castel'
    else:
        type = 'Mountain'
    listOfOneKind = Photo.objects.filter(kind=type)
    coupleOfOneKind = random.sample(listOfOneKind, 2)
    return render(request, 'photos/index.html', {'first': coupleOfOneKind[0], 'second': coupleOfOneKind[1]})


def detail(request, photo_id):
    selected_photo = get_object_or_404(Photo, pk = photo_id)
    selected_photo.match_number +=1
    n = selected_photo.match_number
    selected_photo.votes += 1/n
    selected_photo.save()
    return render(request, 'photos/detail.html', {'photo': selected_photo,})


def losingest(request):
    list = Photo.objects.all()
    minVotePhoto = list[0]
    for x in list:
        if x.votes < minVotePhoto.votes:
            minVotePhoto = x
    return render(request, 'photos/detail.html', {'photo': minVotePhoto,})


def winningest(request):
    list = Photo.objects.all()
    maxVotePhoto = list[0]
    for x in list:
        if x.votes > maxVotePhoto.votes:
            maxVotePhoto = x
    return render(request, 'photos/detail.html', {'photo': maxVotePhoto,})


def daily_photo(request):
    if request.method == 'POST':
        dailyWinner = get_object_or_404(DailyWinner, race_date= request.POST['mydatetime'])
        return render(request, 'photos/detail.html', {'photo': dailyWinner.winnerPhoto, 'date': dailyWinner.race_date, })
    else:
        return render(request, 'photos/daily_photo.html', )


def rank(request):
    return render_to_response('photos/rank.html')

@login_required()
def all_photos(request):
    current_user = request.user.id
    all_photo_list = Photo.objects.filter(createUser_id = current_user)
    #all_photo_list = Photo.objects.all()
    return render(request,'photos/all_photos.html', {'list' : all_photo_list})


@login_required()
def statistic(request):
    current_user = request.user.id
    all_my_photo_list = Photo.objects.filter(createUser_id = current_user)
    #percentuali dei diversi tipi di photo
    count_certain_kind = 0
    for x in all_my_photo_list:
        if x.kind == 'Mountain':
            count_certain_kind +=1
    perc_mountain = 100* count_certain_kind / len(all_my_photo_list)

    count_certain_kind = 0
    for x in all_my_photo_list:
        if x.kind == 'Castel':
            count_certain_kind +=1
    perc_castel = 100* count_certain_kind / len(all_my_photo_list)

    count_certain_kind = 0
    for x in all_my_photo_list:
        if x.kind == 'Beach':
            count_certain_kind +=1
    perc_beach = 100* count_certain_kind / len(all_my_photo_list)

    #occorenze in DailyWinner
    all_daily_winner_list = []
    occurence_count = 0
    for x in DailyWinner.objects.all():
        all_daily_winner_list.append(x.winnerPhoto)
    for x in all_my_photo_list:
        occurence_count += all_daily_winner_list.count(x)
    perc_winner = 100* occurence_count/ len(all_my_photo_list)

    #immagine con punteggio massimo
    maxVotePhoto = all_my_photo_list[0]
    for x in all_my_photo_list:
        if x.votes > maxVotePhoto.votes:
            maxVotePhoto = x
    return render(request, 'photos/statistic.html', {'perc_mountain': perc_mountain, 'perc_castel': perc_castel, 'perc_beach': perc_beach, 'perc_winner': perc_winner, 'photo': maxVotePhoto, })



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
            new_photo.match_number = 0
            new_photo.upload_date = datetime.now()
            new_photo.votes = 50
            new_photo.createUser = request.user
            new_photo.save()
            return render_to_response('portal/personal_space.html')
        else:
            return HttpResponseRedirect('/')
    else:
        form = UploadImageForm()
        return render(request, 'photos/add.html', {'form':form,})



