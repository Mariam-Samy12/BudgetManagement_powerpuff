from django import forms
from .models import Account
from django.core.exceptions import ValidationError
import re  
class SignupForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'username',
            'id': 'username',
            'placeholder': 'example@m1',
           
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'password',
            'id': 'password',
            'minlength': '8',
            
        })
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'confirm_password',
            'minlength': '10',
           
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'email',
            'placeholder': 'fci@gmail.com',
          
        })
    )

    class Meta:
        model = Account
        fields = ['username', 'email', 'password']
    def clean_password(self):
        password=self.cleaned_data.get('password')
        if not re.search(r'[0-9]', password):
            raise ValidationError("Password must contain at least one digit (0-9).")
        if not re.search(r'[A-Z]',password):
            raise ValidationError("Password must contain at least one uppercase letter (A-Z).")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("Password must contain at least one special character (e.g., @, #, $, %).")
        return password
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match. Please try again.")
        return cleaned_data