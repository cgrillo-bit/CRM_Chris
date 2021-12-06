from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Account_executive
from .forms import LeadFormModel
# creating function based views here as prefered by django documentation

# The home function creates the view for the homepage of the CRM
# it takes in a parameter of a request because Django. 
# Django will provide the request to the function when a user goes to a specific page on the website 
# We will be able to see a lot of information from this. This function returns what we want to display. 
# We are going to display the wanted information through a render call
# To have this function work properly we have to add it to the urls in the core_crm. 
def leads_home(request):
    # leads is going to return a Query set
    leads = Lead.objects.all()
    # using context dictonary to fetch and render leads to pass into the django render function
    context = {
        "leads": leads
    }

    return render(request, "leads/leads_home.html", context)


# The lead details function is going to make it possible for the user to click on a lead that has been genereated 
# and take the user to that actual lead. We are accepting request and pk as a paramter. The request is simply that
# pk is hte primary key in the db. We are passing this pk so that we can use it as a unique indentifier in the urls 
# so each lead as its own page. For example we are going to write a path so /leads/2 is assigned to whomever has 
# the primary key of 2 in the db etc. 
def lead_details(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_details.html", context)

#The create_lead method takes in a request as a paramger. It will then assign form to the Lead form class I have created. I have a conditional handling POST as 
# this is a form that creates a lead. If a POST does occur using is_valid Django will check the validity of this form (its a boolean), then using .cleaned_data it cleans 
# the submitted data in a dictonary. As usual it returns a render along with a redirect. This is so when a lead is created it will take us back to the lead list. 
# I realized the hard way that you will accidently create another lead upon re-request without a redirect 
def create_lead(request):
    form = LeadFormModel()
    if request.method == "POST":
        print('Post submit query')
        form = LeadFormModel(request.POST)
        if form.is_valid():
            print("Form validation complete")
            print(form.cleaned_data)

            # Using this cleaned data entered we can pass it to the Lead class as class Lead accepts a first_name, last_name, age, account_executive. 
            # So this is basically grabbing the data entered from the form and keeping it on the server
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            # first grabs the first object in the table as we are just grabing the first account executive available for now. 
            account_executive = Account_executive.objects.first() 
            # this is the actual code that creates the lead in the database 
            Lead.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                account_executive = account_executive
            )
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/create_lead.html", context)