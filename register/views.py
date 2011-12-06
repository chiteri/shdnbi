from django.shortcuts import render_to_response 
from django.template import RequestContext
from shdnbi.register.forms import RegistrationForm
from django.http import HttpResponseRedirect 
# from shdnbi.register.models import Attendee 
from django.conf import settings
import urllib2, json 

# Create your views here.
def registration(request): 
    errors = []
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            participant = Attendee (first_names=cd['first_names'], last_name=cd['last_name'], e_mail=cd['e_mail'], company_organization=cd['company_organization'], short_bio=cd['short_bio'] )
            participant.save() 
            return HttpResponseRedirect('/register/thanks/')
    else: 
        form = RegistrationForm()
    # return render_to_response('register/registration_form.html', {'form':form}, context_instance=RequestContext(request, processors = [custom_proc]) )  
    return render_to_response('register/registration_form.html', {'form':form}, context_instance=RequestContext(request) )	
	
def thank_you(request): 
    return render_to_response('register/thank_you.html')	

# simple wrapper function to encode the username & pass
def encodeUserData(url, app_key, user_key, event_id):
    return u"%s?app_key=%s&user_key=%s&id=%s" % (url, app_key, user_key, event_id)

def access_event(request):	
    link = encodeUserData(settings.EB_URL, settings.EB_APP_KEY, settings.EB_USER_KEY, settings.EB_EVENT_ID)
    res = urllib2.urlopen(link)
    res = json.loads(res.read()) # Convert the JSON string to a Python data structure (dictionary) 
    return  render_to_response('register/attendees_list.html', {'participants':res['attendees']}) # Return a dictionary from the list given 

