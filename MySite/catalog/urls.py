from django.urls import path
from . import views

urlpatterns = [
 path('', views.OrderList.as_view(), name='index'),
 path('order/', views.OrderListArr.as_view(), name='order'),
 path('history/', views.History.as_view(), name='history'),
 path('connect/', views.Connect.as_view(), name='connect'),
 path('createorder/', views.CreateOrder.as_view(), name='createorder'),
]
