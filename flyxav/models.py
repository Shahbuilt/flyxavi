from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    picture = models.FileField()
    location = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    
    # def __str__(self):
    #     return self.Profile

class Passport(models.Model):
    passport_no = models.CharField(max_length=20, null=True)
    passport_file= models.FileField()
    
    # def __str__(self):
    #     return self.passport_no

class Bankdetails(models.Model):
    beneficiary_name = models.CharField(max_length=20, null=True)
    beneficiary_address = models.CharField(max_length=20, null=True)
    beneficiary_country = models.CharField(max_length=20, null=True)
    beneficiary_bank = models.CharField(max_length=20, null=True)
    beneficiary_acnumber = models.CharField(max_length=20, null=True)
    beneficiary_baddress = models.CharField(max_length=20, null=True)
    beneficiary_swiftcode = models.CharField(max_length=20, null=True)
    beneficiary_iban = models.CharField(max_length=20, null=True)
    beneficiary_sortcode = models.CharField(max_length=20, null=True)
    beneficiary_bsb = models.CharField(max_length=20, null=True)
    bank_details= models.FileField()
    
    # def __str__(self):
    #     return self.beneficiary_name    

class invoice(models.Model):
    description = models.CharField(max_length=20, null=True)
    hours = models.CharField(max_length=20, null=True)
    rate = models.CharField(max_length=20, null=True)
    total = models.CharField(max_length=20, null=True)
    # date = models.CharField(max_length=20, null=True)
    # invoice_no = models.CharField(max_length=20, null=True)
    # projectname_dept = models.CharField(max_length=20, null=True)
    # project_description = models.CharField(max_length=20, null=True)
        
    # def __str__(self):
    #     return self.description 
   