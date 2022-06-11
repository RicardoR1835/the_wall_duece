from __future__ import unicode_literals
from django.db import models
import re
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        context = {
            "users": User.objects.all()
        }
        grab = User.objects.filter(email=postData['email'])
        if len(postData['fn']) < 2:
            errors["fn"] = "First name should be more than 2 characters"
        if len(postData['ln']) < 2:
            errors['fn'] = "Last name should be more than 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email not entered in correct form"
        if len(grab) > 0:
            errors['email1'] = "Email already exists"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        if postData['password'] != postData['password_confirm']:
            errors["password_confirm"] = "Passwords do not match"
        return errors

    def login_validator(self, postData):
        errors = {}
        context = {
            "users": User.objects.all()
        }
        email = User.objects.filter(email=postData['email'])
        if len(email) == 0:
            errors["log-email"] = "Email is not registered"
        else:
            user = User.objects.get(email=postData['email'])
            if user.password != postData['password']:
                errors["log-pass"] = "Invalid Credentials"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
    def __repr__(self):
        return f"<Users object: {self.id} ({self.email})>"