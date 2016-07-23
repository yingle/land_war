from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from forms import *

# Create your views here.
def registration_view(request):
    #go to the registration page
    if request.method == 'POST':
        return HttpResponse("You are at the winningest photo.")
    else:
        form = RegistrationForm()
        return render(request, 'registration/registration.html', {'form':form,})
