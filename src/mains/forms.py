from django.forms import widgets
from .models import Student
from django import forms


class StudentForm(forms.ModelForm):
   class Meta:
      model = Student
      fields = ['name',  'age', 'location']

      widgets = {
         'name':forms.TextInput(attrs={'class':'form-control'}),
         'age':forms.TextInput(attrs={'class':'form-control'}),
         'location':forms.TextInput(attrs={'class':'form-control'}),
      }