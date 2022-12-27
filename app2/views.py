from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('first is the best')
def second(request):
    return HttpResponse('second is the best')
