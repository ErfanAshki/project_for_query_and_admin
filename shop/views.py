from django.shortcuts import render
from django.http import HttpResponse

def some_view(request, some):
    return HttpResponse(some)
