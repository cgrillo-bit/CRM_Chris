from django.contrib import admin

from .models import User, Lead, Account_executive


# These admin settings we are registering will allow us to control it from the django admin panel 
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Account_executive)