from django.shortcuts import render
from .models import Food, Consume
# Create your views here.

def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
    else:
        foods = Food.objects.all()
    return render(request, 'myapp/index.html',{'foods':foods})
