from django.urls import path
from .views import (
   ListItem,
   ItemDetailView,
   Cart 
)

app_name='core'

urlpatterns = [
   path('', ListItem.as_view(), name='home'),
   path('shope/<slug>/', ItemDetailView.as_view(), name='detail'),
   path('cart/', Cart.as_view(), name='cart'),

]
  