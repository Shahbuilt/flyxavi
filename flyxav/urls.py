from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('passportsuccess/', views.passportsuccess, name="passportsuccess"),
    path('bankdetailsuccess/', views.bankdetailsuccess, name="bankdetailsuccess"),
    path('descriptionsuccess/', views.descriptionsuccess, name="descriptionsuccess"),
    path('hr_dashboard/', views.hr_dashboard, name="hr_dashboard"),
    
]