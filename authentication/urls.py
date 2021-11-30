from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login_user, name='login'),
<<<<<<< HEAD
    path('hrlogin', views.hrlogin_user, name='hrlogin'),
    path('register', views.register, name='register'),
    path("logout", views.logout_user, name='logout'),
    path('invoice', views.invoice_user, name='invoice'),
=======
    path('register', views.register, name='register'),
    path("logout", views.logout_user, name='logout'),
>>>>>>> a0fa894c9ed4657b4f6c7d8dd1c6430de1fac0e9
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
]
