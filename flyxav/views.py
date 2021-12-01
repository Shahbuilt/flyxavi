from typing import ContextManager
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
    return render(request, 'home.html', {})


@login_required
def dashboard(request):
    if request.method == 'POST':
         print(request.POST)
         data = request.POST
         first_name = request.POST.get('first-name')
         last_name = request.POST.get('last-name')
         location = request.POST.get('location[address]')
         address =  request.POST.get('location[address-2]')
         picture =  request.POST.get('picture')

         profile=Profile.objects.create(first_name=first_name,last_name=last_name,location=location,address=address,picture=picture)
         profile.save()
         return render(request, 'dashboard.html', {})

    
    else:
        return render(request, 'dashboard.html', {})

@login_required
def descriptionsuccess(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        hours = request.POST.get('hours')
        rate = request.POST.get('rate')
        total = request.POST.get('total')
        projectname_dept = request.POST.get('projectname_dept')
        project_description = request.POST.get('project_description')
        
    invoicedetails = Invoicedetails.objects.create(description=description, hours=hours, rate=rate, total=total, projectname_dept=projectname_dept, project_description=project_description)
    passport.save()
    return render(request, 'success.html', {})

@login_required
def passportsuccess(request):
    if request.method == 'POST':
        passport_no = request.POST.get('passport_no')
        passport_file = request.POST.get('passport-file')

    passport = Passport.objects.create(passport_no=passport_no, passport_file=passport_file)
    passport.save()
    return render(request, 'success.html', {})

@login_required
def hr_dashboard(request):
    passport= Passport.objects.all() 
    print(passport)
    Context = {
        'passport':passport
    }
    return render(request, 'hr_dashboard.html', Context)

@login_required
def bankdetailsuccess(request):
    if request.method == 'POST':
        beneficiary_name = request.POST.get('beneficiary_name')
        beneficiary_address = request.POST.get('beneficiary_address')
        beneficiary_country = request.POST.get('beneficiary_country')
        beneficiary_bank = request.POST.get('beneficiary_bank')
        beneficiary_baddress = request.POST.get('beneficiary_baddress')
        beneficiary_swiftcode = request.POST.get('beneficiary_swiftcode')
        beneficiary_iban = request.POST.get('beneficiary_iban')
        beneficiary_sortcode = request.POST.get('beneficiary_sortcode')
        beneficiary_bsb = request.POST.get('beneficiary_bsb')

        bank_details = request.POST.get('bank_details')

    bankdetailsuccess = bankdetails.objects.create(bank_details=bank_details, beneficiary_name=beneficiary_name, beneficiary_address=beneficiary_address,beneficiary_country=beneficiary_country, beneficiary_bank=beneficiary_bank, beneficiary_baddress=beneficiary_baddress, beneficiary_swiftcode=beneficiary_swiftcode, beneficiary_iban=beneficiary_iban, beneficiary_sortcode=beneficiary_sortcode, beneficiary_bsb=beneficiary_bsb)
    bankdetails.save()

    return render(request, 'success.html', {})