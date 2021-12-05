from django.contrib import admin
from django.urls import path

from leads.views import home

# url patterns holds the forwarding for the pages the user is going to visit. For example if we types in /home in the browser
# it will present the information that we have set the path for /home. empty path is going to handle the path when no forwardinng / is added to url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
