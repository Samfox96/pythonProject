from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, 'home.html')


def new(request):
    return render(request, 'About us.html')


def customer(request):
    form = ContactForm()
    return render(request, 'form.html', {'form': form})


def customer(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        print(name, email)
    form = ContactForm()
    return render(request, 'form.html', {'form': form})


def future(request):
    return render(request, 'The Future.html')


def weather(request):
    return render(request, 'Weather.html')

