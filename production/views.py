from django.shortcuts import render
from django.http import HttpResponse
from .models import Prod


def index(request):
    products = Prod.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New product')
