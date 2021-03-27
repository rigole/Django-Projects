from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('item', views.item, name = 'item'),
    path('goal',views.goal, name='goal'),
    #path for item
    path('<int:item_id>/',views.id,name='id'),
    # add item formular path
    path('add',views.create_item, name="create_item"),


]
