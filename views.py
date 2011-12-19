from django.views.generic.simple import direct_to_template
from django.template import RequestContext 
from shdnbi.context_processors import custom_proc
from shdnbi.post.models import Post
	
def home(request): 
    # return direct_to_template(request, 'base.html', context_instance=RequestContext(request, processors = [custom_proc]))
    return direct_to_template(request, 'base.html', {'featured_posts': Post.objects.filter(featured=True) } ) 
	
def follow(request): 
    return direct_to_template(request, 'follow_button.htm')