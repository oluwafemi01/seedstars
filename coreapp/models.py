from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class stores(models.Model):
    firstname = models.CharField(max_length=90)
    lastname = models.CharField(max_length=70)
    emailadd = models.EmailField(null= False, unique=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.firstname
