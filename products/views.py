from django.http import HttpResponse
from django.shortcuts import render

# /products => index
def index(request):
    return HttpResponse('Hello pabtab')


def new(request):
    return HttpResponse('New products')

