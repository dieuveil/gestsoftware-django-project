from django.urls import path
from .views import formation_ia


urlpatterns = [
    path('/formation-ia', formation_ia),
]