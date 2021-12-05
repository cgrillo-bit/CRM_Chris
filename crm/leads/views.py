from django.shortcuts import render
from django.http import HttpResponse
# creating function based views here as prefered by django documentation

# The home function creates the view for the homepage of the CRM
# it takes in a parameter of a request because Django. 
# Django will provide the request to the function when a user goes to a specific page on the website 
# We will be able to see a lot of information from this. This function returns what we want to display. 
# We are going to display the wanted information through a render call
# To have this function work properly we have to add it to the urls in the core_crm. 
def home(request):
    return render(request, "home.html")