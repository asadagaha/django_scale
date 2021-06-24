from django import forms
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.admin.widgets import AdminDateWidget

class UserForm(forms.Form):
    weight = forms.FloatField(label='体重(kg)')


class CustomUserCreationForm(UserCreationForm): 
  class Meta:

    model  = get_user_model() 
    fields = (
      'birth',
      'sex',
      'height',
      'email',) 
    widgets = {
      'birth': forms.SelectDateWidget(years=[x for x in range(1990, 2030)]),
      }