from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import CreateView

from .models import Order


class OrderList(generic.ListView):
    model = Order
    template_name = 'index.html'


class OrderListArr(generic.ListView):
    model = Order
    template_name = 'order.html'


class History(generic.ListView):
    model = Order
    template_name = 'history.html'


class Connect(generic.ListView):
    model = Order
    template_name = 'connect.html'


class CreateOrder(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['name', 'text_order', 'image', 'price']
    template_name = 'createorder.html'
    success_url = '/catalog/'


