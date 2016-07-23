from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import Permission
from forms import *

# Create your views here.
def registration_view(request):
    #go to the registration page
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            new_user = User.objects.create_user(username, email, password)
            new_user.is_active = True
            #give permession to add photos
            permission = Permission.objects.get(name='Can add photo')
            new_user.user_permissions.add(permission)
            new_user.save()
            return render_to_response('registration/success.html')
        else:
            return render_to_response('registration/unsuccess.html')
    else:
        form = CreateUserForm()
        return render(request, 'registration/registration.html', {'form':form,})
