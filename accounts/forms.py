from django import forms
from django.contrib.auth.forms import (
    UserCreationForm
)
from .models import User

class SignupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','first_name','last_name','gender','phone_number','rating']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar','first_name','last_name','gender',
                  'phone_number', 'rating']