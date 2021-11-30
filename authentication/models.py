from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
<<<<<<< HEAD
    
    mobile = models.CharField(max_length=15,null=True)
    resume = models.FileField()
    
    def __str__(self):
        return self.email


    
   
    
    
=======
    resume = models.FileField()

    def __str__(self):
        return self.email
>>>>>>> a0fa894c9ed4657b4f6c7d8dd1c6430de1fac0e9
