from django.urls import path
 
# importing views from views..py
from .views import incubateur, index
from .views import about
from .views import formation
from .views import incubateur
from .views import startup
from .views import webdeveloper
 
urlpatterns = [
    path('', index),
    path('about', about),
    path('formation', formation),
    path('startup', startup),
    path('incubateur', incubateur),
    path('web-developer', webdeveloper),
]