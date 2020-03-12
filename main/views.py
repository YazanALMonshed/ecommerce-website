from django.shortcuts import render
from .models import Item
# Create your views here.



def all_items(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'index.html', context)