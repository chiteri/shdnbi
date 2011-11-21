from django.conf.urls.defaults import * 
from shdnbi.register.models import Attendee 

# Create your views here.
urlpatterns = patterns('shdnbi.register.views', 
    (r'^$', 'registration'),
    (r'^thanks/$', 'thank_you' ), 
) 

attendee_info_dict = {
    'queryset': Attendee.objects.all(),
}

urlpatterns += patterns('django.views.generic', 
    (r'^enrolled/$', 'list_detail.object_list', dict(attendee_info_dict, paginate_by=20)),
) 

#post_info_dict = {
#    'queryset': Post.objects.all(),
#    'date_field': 'pub_date',
#}
#urlpatterns += patterns('django.views.generic', 
#    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'date_based.object_detail', post_info_dict),
#)
