from django.contrib import admin 
from shdnbi.register.models import Attendee

class AttendeeAdmin(admin.ModelAdmin): 
    pass 
	
admin.site.register(Attendee, AttendeeAdmin)