from django.template import RequestContext 
from shdnbi.post.models import Post

def custom_proc(Request): 
    # A context processor that provides a list of the featured Posts
    return { 'FEATURED_POSTS': Post.objects.filter(featured=True)}