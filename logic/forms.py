from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={'class': 'input-val bg-transparent form-control form-control-lg mt-3'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password2'].widget.attrs['class'] = 'input-val bg-transparent  form-control form-control-lg mt-3'
        self.fields['username'].widget.attrs['class'] = 'input-val bg-transparent form-control form-control-lg mt-3'
        self.fields['password1'].widget.attrs['class'] = 'input-val bg-transparent form-control form-control-lg mt-3'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

