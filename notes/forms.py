from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm


class NoteCreationForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "description", "draft", "saved"]


class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "description", "draft", "saved"]

class AccountSettingsForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  