from django.views.generic.simple import direct_to_template
	
def home(request): 
    # return direct_to_template(request, 'base.html', context_instance=RequestContext(request, processors = [custom_proc]) 
    return direct_to_template(request, 'base.html' )
	