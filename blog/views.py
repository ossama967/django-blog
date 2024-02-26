from django.shortcuts import render
from django.http import HttpResponse

import inspect

# Create your views here.
def my_blog(request):
    return HttpResponse('Hello, important!')

def my_love(request):
    tintin ='HAHAHA'
    return HttpResponse(tintin)
    

