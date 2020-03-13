from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Item
# Create your views here.





class ListItem(ListView):
    model = Item
    template_name = 'index.html'



class ItemDetailView(DetailView):
    model = Item
    template_name = "shop-single.html"


class Cart(ListView):
    model = Item
    template_name = 'cart.html'



