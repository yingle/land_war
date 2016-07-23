from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def main_page(request):
    return render_to_response('main_page.html')


def logout_view(request):
    "Log users out and re-direct them to the main page."
    logout(request)
    return HttpResponseRedirect('/')

