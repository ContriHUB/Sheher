from django.forms import ModelForm
from .models import VisitorDetails

class EditProfileForm(ModelForm):
    class Meta:
        model = VisitorDetails
        fields = [ 'city', 'address', 'phone', 'sos_contact', 'gender', 'profile_picture']