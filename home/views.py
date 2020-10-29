from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting, ContactForm, ContactMessage


def index(request):
    setting = Setting.objects.get(pk=1),
    page = "home",
    context = {'setting': setting, 'page': page}
    return render(request, 'index.html', context)

def aboutus(request):
    setting = Setting.objects.get(pk=1),
    context = {'setting': setting}
    return render(request, 'about.html', context)

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent. Thank you.")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1),
    form = ContactForm
    context = {'setting': setting,'form': form}
    return render(request, 'contactus.html', context)


