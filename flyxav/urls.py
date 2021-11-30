from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
<<<<<<< HEAD
    path('passportsuccess/', views.passportsuccess, name="passportsuccess"),
    path('hr_dashboard/', views.hr_dashboard, name="hr_dashboard"),
=======
>>>>>>> a0fa894c9ed4657b4f6c7d8dd1c6430de1fac0e9
    
]