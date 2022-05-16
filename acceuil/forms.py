from pyexpat import model
from django import forms
from .models import Students

class Studentsform(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['fname', 'lname', 'email', 'messages']
