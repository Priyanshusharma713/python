from django import forms
from .models import UserModel,product

class Userform(forms.Form):
    name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    contact=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))

class userModelform(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=['name','contact']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            
        }


class Productmodelform(forms.ModelForm):
    class Meta:
        model=product
        fields="__all__"
        widgets={
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
        }
