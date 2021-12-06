from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
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
    return render(request, "leads/lead_detail.html", context)