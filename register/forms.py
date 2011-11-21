from shdnbi.register.models import Attendee 
from django.forms import ModelForm 

class RegistrationForm(ModelForm):
    class Meta:
        model = Attendee  
        # exclude = ('applicant', 'application_date', 'days_requested', 'status', 'approved_by', 'approval_date', )

