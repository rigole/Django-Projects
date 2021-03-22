from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def item (request):
    return HttpResponse('This s an Item view')
def goal (request):
    return HttpResponse('<h1>I am on the way to success and I will be a Billionaire</h1>')
