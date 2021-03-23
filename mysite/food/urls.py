from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name = 'index'),
    path('item', views.item, name = 'item'),
    path('goal',views.goal, name='goal'),
    #path for item
    path('<int:item_id>/',views.id,name='id'),

]
