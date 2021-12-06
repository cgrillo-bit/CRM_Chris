from django.urls import path
from .views import lead_details, leads_home

# Doing this to clean up url paths as the urls.py in the main application will load every single path one by one
# It is common django convention here to do this method 

app_name = "leads"

urlpatterns = [
    path('', leads_home),
    path('<pk>/', lead_details)
]
