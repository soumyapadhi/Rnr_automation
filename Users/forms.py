from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Users.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,help_text='Required')
    last_name = forms.CharField(max_length=30,help_text='Required')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'birth_date', 'email', )
