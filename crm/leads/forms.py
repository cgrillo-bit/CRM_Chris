from django import forms 
from .models import Lead


# We are creating a form class from Django forms to use this whenever wee need a form. Lucky for us Django has this built in. I love this frameowkr
class LeadFormModel(forms.ModelForm):
    # Django model form requires you to make a Meta class. 
    class Meta:
        model = Lead
        # Per django documentation we need the ModelForm to have "fields"
        fields = (
            'first_name',
            'last_name',
            'age',
            'account_executive',
        )


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=1)