from django.conf.urls.defaults import * 
from shdnbi.post.models import Post 

# Create your views here.
post_info_dict = {
    'queryset': Post.objects.all(),
}

urlpatterns = patterns('django.views.generic', 
    (r'^$', 'list_detail.object_list', dict(post_info_dict, paginate_by=5)),
) 

post_info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'pub_date',
}
urlpatterns += patterns('django.views.generic', 
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'date_based.object_detail', post_info_dict),
)
