from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name = 'index'),
    path('item', views.item, name = 'item'),
    path('goal',views.goal, name='goal'),
    #path for item
    path('<int:pk>/',views.FoodDetail.as_view(),name='details'),

    # add item formular path
    path('add',views.CreateItem.as_view(), name="create_item"),

    # edit item path
    path('update/<int:id>', views.update_item,name='update_item'),

    #Delete item
    path('delete/<int:id>/', views.delete_item,name="delete_item")





]
