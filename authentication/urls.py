from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login_user, name='login'),
    path('hrlogin', views.hrlogin_user, name='hrlogin'),
    path('register', views.register, name='register'),
    path("logout", views.logout_user, name='logout'),
    path('invoice', views.invoice_user, name='invoice'),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
]
