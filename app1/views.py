from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('function is a block ')
def second(request):
    return HttpResponse('function is called after function declaration')