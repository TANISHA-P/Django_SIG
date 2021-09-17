from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

choice = (
    ("M","Male"),
    ("F","Female"),
    ("O","Other")
)
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    gender = forms.ChoiceField(choices = choice)
    mobile = forms.IntegerField()
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','gender','mobile','email','password1','password2')
