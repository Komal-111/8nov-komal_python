from django import forms
from .models import products

class productForm(forms.ModelForm):
    class Meta:
        model=products
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=products
        fields=['productname','productprice','productrame','productcatagory']