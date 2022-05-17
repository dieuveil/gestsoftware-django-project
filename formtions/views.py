from email import message

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse




def formation_ia(request):
    return render(request, "formation-ia.html")


