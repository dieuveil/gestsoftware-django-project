from email import message
import imp
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

from .models import Students
from .forms import Studentsform

def index(request):
    if request.method == "POST":
       form = Studentsform(request.POST or None)
       if form.is_valid():
           form.save()
           return render(request, 'index.html', {})
    else:
       return render(request, 'index.html', {})




  
# create a function
def about(request):
    return render(request, "about.html")


# create a function
def formation(request):
    return render(request, "formation.html")

# create a function
def startup(request):
    return render(request, "startup.html")

# create a function
def incubateur(request):
    return render(request, "incubateur.html")

# create a function
def webdeveloper(request):
    return render(request, "webdeveloper.html")

def mobiledeveloper(request):
    return render(request, "mobiledeveloper.html")

def bigdata(request):
    return render(request, "bigdata.html")

def datascience(request):
    return render(request, "datascience.html")

def business(request):
    return render(request, "business.html")

def pydeveloper(request):
    return render(request, "pythondeveloper.html")


