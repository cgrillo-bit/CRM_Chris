from django.urls import path
from .views import lead_details, leads_home, create_lead, update_lead, delete_lead

# Doing this to clean up url paths as the urls.py in the main application will load every single path one by one
# It is common django convention here to do this method 

app_name = "leads"

urlpatterns = [
    path('', leads_home, name='leads-home'),
    path('<int:pk>/', lead_details, name='lead-details'),
    path('<int:pk>/update/', update_lead, name='update-lead'),
    path('<int:pk>/delete/', delete_lead, name='delete-lead'),
    path('create/', create_lead, name='create-lead'),
]
