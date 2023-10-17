from django.urls import path
from . import views

urlpatterns = [
    path('stock/', views.stock_item_list, name='stock_item_list'),
]
