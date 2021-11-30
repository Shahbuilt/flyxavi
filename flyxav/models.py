from django.db import models

# Create your models here.
<<<<<<< HEAD

class Profile(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    picture = models.FileField()
    location = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.first_name

class Passport(models.Model):
    passport_no = models.CharField(max_length=20, null=True)
    passport_file= models.FileField()
    
    def __str__(self):
        return self.passport_no

    
   
=======
>>>>>>> a0fa894c9ed4657b4f6c7d8dd1c6430de1fac0e9
