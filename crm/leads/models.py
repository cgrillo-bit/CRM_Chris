from django.db import models
from django.contrib.auth.models import AbstractUser


# Creating custom user moduel as recommended by Django documentation
# Just writing pass to pass the default this way. Its 3am I am not writing a 
# custom user class. 
class User(AbstractUser):
    pass 

# Writing database scheme models for leads application - we do need a table. The Best Run 
# The general idea of this is going to hold the data that one would find in leads
# names are strings this is what character field ages are numbers so we use IntegerField that is greater than 0 with default 
# all other fields I want to create will be added respectively 
# In this model I am going to delcare all of the data that I need in connection to leads
class Lead(models.Model):
    # Making a tuple for options that can be selected as a source 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0) 
    account_executive = models.ForeignKey("Account_executive", on_delete=models.CASCADE)
    # What were doing here is deleting the lead if the case our account executive gets
    # removed from the database
    # --TODO add warning what leads will be deleted when account executive is being deleted
    # After an hour of digging through documentation I realized that having this line under Account_executive means there can only be 
    # One lead per account executive. Nice Chris - I'm slowly going insane as I need to get a 100 and I usually get paid to be tortued in this fashion.
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    # Table relationship code starts here
class Account_executive(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email