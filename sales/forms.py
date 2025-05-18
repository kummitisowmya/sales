from django import forms
from .models import TrainingClass
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class TrainingClassForm(forms.ModelForm):
    class Meta:
        model = TrainingClass
        fields = ['name', 'description', 'start_date', 'end_date']  # Add relevant fields


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ['username', 'email', 'password1', 'password2']  # Add fields as needed