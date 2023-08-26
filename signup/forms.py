from django import forms
from .models import UserProfile

class SignupForm(forms.ModelForm):
    """
    A form for user signup.
    """
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Render the password field as a password input
        }
