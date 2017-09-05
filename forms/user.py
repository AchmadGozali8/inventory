from django import forms
from django.contrib.auth.models import User
from companies.models import Company

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
           'password': forms.PasswordInput(),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'department')
        widgets = {
            'name': form.Select(attrs={'class': 'form-control show-tick')),
            'department': form.Select(attrs={'class': 'form-control show-tick')),
        }
