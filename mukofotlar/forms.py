from  django.forms import  ModelForm
from django import forms
from .models import Prize

class PrizeForm(ModelForm):
    class Meta:
         model=Prize
         fields=['name','age','category','info','image']

         labels = {
                'name': 'Prize Name',
                'age': 'Age',
                'category': 'Category',
                'info': 'Info',
                'image': 'Prize Image',
            }

