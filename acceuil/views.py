from email import message
import imp
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

from .models import Students

# Create your views here.

  
# create a function
#def index(request):
    
    # return response with template and context
    #return render(request, "index.html", context)

def index(request):
    all_students = Students.objects.all
    if request.method == "POST":
       message_name = request.POST['message-name']
       message_email = request.POST['message-email']
       message_subject = request.POST['message-subject']
       message = request.POST['message']
       receiver = 'dieuveilmabirou@gmail.com'

       send_mail(
         message_subject,
         message,
         message_email,
         [receiver],
       )

       return render(request, 'index.html', {'message_name': message_name})
    else:
       return render(request, 'index.html', {'all': all_students})




  
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


