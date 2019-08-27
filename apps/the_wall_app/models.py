from __future__ import unicode_literals
from django.db import models
import re, bcrypt

# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument! copy
# (just parts, like request.POST)
class UserManager(models.Manager):
    def basic_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        PASS_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 1:
            errors["first_name"] = "Please input a first name."
        if not NAME_REGEX.match(postData['first_name']):
            errors["first_name2"] = "Please provide a first name without any special characters."
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Please input a last name."
        if not NAME_REGEX.match(postData['last_name']):
            errors["last_name2"] = "Please provide a last name without any special characters."
        if len(postData['email']) < 1:
            errors["email"] = "Please provide an email."
        if not EMAIL_REGEX.match(postData['email']):
            errors["email3"] = "Invalid email address!"
        if len(['email']) > 2:
            print("email longer then 2 tripped")
            email = postData['email']
            email_hunt = {
                "email": email
            }
            email_check = user.objects.filter(email_hunt)
            if email_check == True:
                print("email check tripped")
                errors["email2"] = "That email address is in use."
        if len(postData['password']) < 1:
            errors["password"] = "Please provide a password."
            print("Please provide a password." )
        if not PASS_REGEX.match(postData['password']):
            errors["password2"] = "Please provide a password made without any special characters, like ?!@#$%^&*()<>}{[]:'."
        if postData['password'] != postData['con_password']:
            errors["password3"] = "Password doesn't match."
            print("Password doesn't match.")
        print("good to go!")
        return errors
    def login_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PASS_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address!"
        if not user.objects.filter(email= postData['email']):
            errors['email2']
        elif len(postData['email']) < 1:
            errors["email3"] = "Please provide an email."
        else:
            if not PASS_REGEX.match(postData['password']):
                errors["password2"] = "Please provide a password made without any special characters, like ?!@#$%^&*()<>}{[]:'."
            if not bcrypt.checkpw(postData['password'].encode(), user.objects.filter(email= postData['email'])[0].password.encode()):
                errors['password'] = "Invalid password."
        return errors
    def message_validator(self, postData):
        # TEXT_REGEX = re.compile(r'^[a-zA-Z0-9.!?+_-]+$')
        errors = {}
        str = postData['message_content']
        x = re.findall("[|/<>'}{]", str)
        if len(x) > 0:
            errors["message_content"] = "Please avoid using characters like |/<>'}{ in your message!"
        return errors
    def comment_validator(self, postData):
        # TEXT_REGEX = re.compile(r'^[a-zA-Z0-9.!?"(),;:+_-]+$')
        errors = {}
        str = postData['comment_content']
        x = re.findall("[|/<>'}{]", str)
        if len(x) > 0:
            errors["comment_content"] = "Please avoid using characters like |/<>'}{ in your comment!"
        return errors

# x.match(postData['message_content'])
# (r'^[a-zA-Z0-9.!?"(),;:+_-]+$')

class user(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()    # add this line!

class message(models.Model):
    message_owner = models.ForeignKey(user, related_name="messages")
    message_content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()    # add this line!

class comment(models.Model):
    comment_owner = models.ForeignKey(user, related_name="comments")
    message_attached = models.ForeignKey(message, related_name="attached_comments")
    comment_content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()    # add this line!