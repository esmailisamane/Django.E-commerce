from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    university = 'xxx'
    dept = 'comp'
    context = {'university': university, 'department': dept}
    return render(request, 'index.html', context)
