from typing import ContextManager
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile,Passport

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