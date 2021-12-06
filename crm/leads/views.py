from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Account_executive
from .forms import LeadForm, LeadFormModel
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

            # Django model form allows us to call the save method to save all data entered as a new lead, BAM. If you wanted to create your own lead you would need to
            # declare each form entry specifically. 
            form.save() 
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/create_lead.html", context)

# The update lead function is going to allow us to update existing leads, it takes in request (THESE FUNCTIONS WILL ALWAYS TAKE IN REQUEST AS IT IS A BROWSER REQUEST TO MANIPULATE XYZ)
# We are also having the primary key as a paramater as that is how we are referring to the leads at this time. So basically we have the same function as the create lead however,
# now on the LeadFormModel we are passing this a parameter called instance=lead, therefore when going to /update the field will be prepopulated. Very nice. 
def update_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadFormModel(instance=lead)
    if request.method == "POST":
        form = LeadFormModel(request.POST, instance=lead)
        if form.is_valid():
            lead.save()
            print("Form update complete")
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead,
        
    }
    return render (request, "leads/update_lead.html", context)


# The delete lead key does exactly what it says. It will grab the lead from the database. It is taking request and primary key as parameters as usual. We are going to grab
# the referenced lead from the DB using that primary key and using a native Django method .delete() we will be able to delete this lead with no issues. After a lead is deleted
# we are going to return a render back to the leads page, Workflow as followed: Select lead -> User goes to delete_lead view-> lead is deleted from DB and redirect back to page showing 
# all of the leads. 
def delete_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete() 
    return redirect("/leads")