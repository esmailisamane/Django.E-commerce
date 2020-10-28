from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=1),
    page = "home",
    context = {'setting': setting, 'page':page}
    return render(request, 'index.html', context)

def aboutus(request):
    setting = Setting.objects.get(pk=1),
    context = {'setting': setting}
    return render(request, 'about.html', context)

def contact(request):
    # setting = Setting.objects.get(pk=1),
    # context = {'setting': setting}
    # return render(request, 'content.html', context)
    return HttpResponse("ddd")