from django.db import models

# Create your models here.
class Attendee(models.Model): 
    # Core Fields 
    first_names = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    e_mail = models.EmailField(blank=False) 
    
	# Meta Information 
    company_organization = models.CharField(max_length=50, blank=False, help_text="Company or organization") 
    short_bio = models.TextField(blank=False, help_text="(e.g Hacker, Developer, Scientist, Researcher)")	
	
    class Meta: 
        ordering = ['first_names', 'last_name']
		
    def __unicode__(self): 
        return u'%s, %s from: %s'%(self.first_names, self.last_name, self.company_organization.upper())
		
    def get_absolute_url(self): 
        return '/attendees/%s/%s/%s/'%(self.first_names.lower(), self.last_name.lower(), self.company_organization.lower())
    
