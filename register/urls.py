from django.conf.urls.defaults import * 
from shdnbi.register.models import Attendee 

# Create your views here.
# urlpatterns = patterns('shdnbi.register.views', 
#    (r'^$', 'registration'),
#    (r'^thanks/$', 'thank_you' ), 
#) 

#attendee_info_dict = {
#    'queryset': Attendee.objects.all(),
#}

# urlpatterns += patterns('shdnbi.register.views', 
#    (r'^enrolled/$', 'access_event'),
#) 

urlpatterns = patterns('shdnbi.register.views', 
    (r'^$', 'access_event'),
) 
