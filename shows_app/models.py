from distutils import errors
from ssl import create_default_context
from unittest.util import _MAX_LENGTH
from django.db import models


class ShowManager(models.Manager):
    def validate_show(request,form_data):
        errors = {}
        if len(form_data['title'])<2:
            errors['title'] = "Title should be at lest 2 characters"
        if len(form_data['network'])<3:
            errors['network'] = "Network should be at lest 3 characters"
        if len(form_data['description'])<10:
            errors['description'] = "Description should be at lest 10 characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description  = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()














class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password  = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # objects = ShowManager()
