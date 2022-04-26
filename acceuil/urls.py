from django.urls import path
 
# importing views from views..py
from .views import index
from .views import about
 
urlpatterns = [
    path('', index),
    path('about', about),
]