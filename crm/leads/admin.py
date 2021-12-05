from django.contrib import admin

from .models import User, Lead, Account_executive

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Account_executive)