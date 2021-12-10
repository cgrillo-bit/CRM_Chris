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
    company = models.CharField(max_length=40, default="")
    industry = models.CharField(max_length=30, default="")
    phone_number = models.IntegerField(default=0)
    description = models.CharField(max_length=500, default="")
     
    account_executive = models.ForeignKey("Account_executive", on_delete=models.CASCADE)
    # What were doing here is deleting the lead if the case our account executive gets
    # removed from the database
    # After an hour of digging through documentation I realized that having this line under Account_executive means there can only be 
    # One lead per account executive. Nice Chris - I'm slowly going insane as I need to get a 100 and I usually get paid to be tortued in this fashion.
    # This __str__ function is just going to retunr fields first name, last name and company assigned 
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.company}"
    # Table relationship code starts here

    # this class is hadling the account executives we have assinged note there is only one account executive in the system. The .CASCADE is being used such that 
    # when a changes are made to the user model it will also delete anything attached to it 
class Account_executive(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# We are using this function to reuturn the user email 
    def __str__(self):
        return self.user.email