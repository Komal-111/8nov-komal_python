from django import forms
from .models import signup


class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'

