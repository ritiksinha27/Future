from django import forms
from django.forms import ModelForm,widgets
from app.models import *
class registerForm(forms.Form):
    name=forms.CharField(max_length=25, required=True)
    email=forms.EmailField( required=True)
    phone=forms.IntegerField( required=True)
    
class coourse_edit(forms.ModelForm):
    # description=forms.TextInput()
    # price=forms.FloatField(required=True)
    # highlight=forms.Textarea()
    # photo=forms.FileInput(uploadto='images/')
    class Meta:
        model = Course
        fields = "__all__"
        widgets ={
            'category' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'highlight' : forms.TextInput(attrs={'class':'form-control','style':'height:100px','rows':4}),
            # 'photo' : forms.FileInput(attrs={'class':'form-control'})
        }