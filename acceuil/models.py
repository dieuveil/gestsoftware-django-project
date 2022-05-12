from django.db import models

# Create your models here.
class Students(models.Model):
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    messages= models.CharField(max_length=200)
