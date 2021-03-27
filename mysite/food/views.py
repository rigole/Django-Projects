from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ItemForm
from .models import Item
from django.template import  loader
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    #rendring an html file using template

    #template = loader.get_template('food/index.html')

    # context here is used to pass database element to the template
    context= {
          'item_list': item_list,
    }
    return render(request,'food/index.html', context)

# view of the item
def item (request):
    return HttpResponse('This s an Item view')

def goal (request):
    return HttpResponse('<h1>I am on the way to success and I will be a Billionaire</h1>')

# view to display item_id on click
def id(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/details.html', context)

#view of form to add items
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form',{'form':form})