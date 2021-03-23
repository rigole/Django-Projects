from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import  loader
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context= {

    }
    return HttpResponse(template.render(context,request))

def item (request):
    return HttpResponse('This s an Item view')

def goal (request):
    return HttpResponse('<h1>I am on the way to success and I will be a Billionaire</h1>')


