from django.db import models
from datetime import datetime
import re

class UserManager(models.Manager):
    def registration_validator(self, postdata):
        errors = {}
        ##username
        if len(postdata['username']) == 0:
            errors['username'] = "Need a username"
        if len(User.objects.filter(username=postdata['username'])) != 0:
            errors['username'] = "Username already taken!"
            
        ##first_name
        if len(postdata['first_name']) == 0:
            errors['first_name'] = "First Name required"
        else:
            c=postdata['first_name']
            if not c.isalpha():
                errors['first_name'] = "Invalid characters"
            elif len(postdata['first_name']) == 1:
                errors['first_name'] = "Needs to be longer than 1 character"
        
        ##last_name
        if len(postdata['last_name']) == 0:
            errors['last_name'] = "Last Name required"
        else:
            c=postdata['last_name']
            if not c.isalpha():
                errors['last_name'] = "Invalid characters"
            elif len(postdata['last_name']) == 1:
                errors['last_name'] = "Needs to be longer than 1 character"

        ##email
        if len(postdata['email']) == 0:
            errors['email'] = "Email required"
        else:
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postdata['email']):         
                errors['email'] = ("Email address-invalid format")
            elif len(User.objects.filter(email=postdata['email'])) != 0:
                errors['email'] = "Email Address already used!"
        
        ##password
        if len(postdata['password']) == 0:
            errors['password'] = "Password required"
        if len(postdata['password']) >= 1 and len(postdata['password']) <= 7:
            errors['password'] = "Password too short.  Atleast 8 characters"

        ##password confirmation
        if postdata['password'] != postdata['password_confirm']:
            errors['password_confirm'] = "Password Confirmation Failed.  Try Again."

        return errors




class User(models.Model):
    username=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #puzzles
    #brands
    #categories
    #projects
    #helpers

    def __repr__(self):
        return f"**User:{self.first_name}**"