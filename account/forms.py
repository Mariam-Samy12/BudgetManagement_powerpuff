from django import forms
from .models import Account

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
            'minlength': '10',
            
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