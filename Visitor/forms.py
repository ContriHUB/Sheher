from django import forms

class EditProfileForm(forms.Form):
    GENDER = (
        (1,'MALE'),
        (2,'FEMALE')
    )
    first_name=forms.CharField(label='first_name',max_length=255)
    last_name = forms.CharField(label='last_name',max_length=255)
    address=forms.CharField(label='address',max_length=255)
    phone=forms.CharField(label='phone',max_length=10)
    sos_contact=forms.CharField(label='sos_contact',max_length=10)
    gender=forms.CharField(label='gender',widget=forms.RadioSelect(choices=GENDER))