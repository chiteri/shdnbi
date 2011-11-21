from django.shortcuts import render_to_response 
from django.template import RequestContext
from shdnbi.register.forms import RegistrationForm
from django.http import HttpResponseRedirect 
from shdnbi.register.models import Attendee 

# Create your views here.
def registration(request): 
    errors = []
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            participant = Attendee (first_names=cd['first_names'], last_name=cd['last_name'], e_mail=cd['e_mail'], company_organization=cd['company_organization'], short_bio=cd['short_bio'] )
            participant.save()
            #    cd['subject'],
            #    cd['message'],
            #    cd.get('e_mail', 'martin.chiteri@gmail.com'),
            #   ['chiteri@geek.co.ke'], fail_silently=False)
            return HttpResponseRedirect('/register/thanks/')
    else: 
        form = RegistrationForm()
    # return render_to_response('register/registration_form.html', {'form':form}, context_instance=RequestContext(request, processors = [custom_proc]) )  
    return render_to_response('register/registration_form.html', {'form':form}, context_instance=RequestContext(request) )	
	
def thank_you(request): 
    return render_to_response('register/thank_you.html')
