from django import forms
from .models import usersignup

class userForm(forms.ModelForm):
    
    class Meta:
        model=usersignup
        fields='__all__'
        
class updateForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields=['username','passward']