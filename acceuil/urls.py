from django.urls import path
 
# importing views from views..py
from .views import index
from .views import about
from .views import formation
from .views import webdeveloper
 
urlpatterns = [
    path('', index),
    path('about', about),
    path('formation', formation),
    path('web-developer', webdeveloper),
]