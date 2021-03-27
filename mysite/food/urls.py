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
    # edit item path
    path('update/<int:id>', views.update_item,name='update_item'),
    #Delete item
    path('delete/<int:id>/', views.delete_item,name="delete_item")





]
