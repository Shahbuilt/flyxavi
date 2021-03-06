from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    
    mobile = models.CharField(max_length=15,null=True)
    resume = models.FileField()
    
    def __str__(self):
        return self.email


    
   
    
    