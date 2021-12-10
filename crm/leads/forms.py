from django import forms 
from .models import Lead, User
from django.contrib.auth.forms import UserCreationForm, UsernameField

# We are creating a form class from Django forms to use this whenever wee need a form. Lucky for us Django has this built in. I love this frameowkr
class LeadFormModel(forms.ModelForm):
    # Django model form requires you to make a Meta class. 
    class Meta:
        model = Lead
        # Per django documentation we need the ModelForm to have "fields"
        fields = (
            'first_name',
            'last_name',
            'company',
            'industry',
            'phone_number',
            'account_executive',
            'description',
        )

# This class is going to greate fields and columns in the database of the entries of the form 
class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    company = forms.CharField()
    industry = forms.CharField()
    phone_number = forms.IntegerField()
    description = forms.CharField() 

# We are using this class to override the standard create user form. 
class CUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
