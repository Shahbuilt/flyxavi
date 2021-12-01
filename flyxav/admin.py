from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
	list_display = ('user', 'location')
	list_search_fields = ('user', 'location')
    
admin.site.register(Passport)
admin.site.register(Bankdetails)
admin.site.register(invoice)