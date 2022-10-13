from django import forms

class EditProfileForm(forms.Form):
    GENDER = (
        (1,'MALE'),
        (2,'FEMALE'),
        (3,'OTHERS'),
    )
    first_name=forms.CharField(label='First Name',max_length=255)
    last_name = forms.CharField(label='Last Name',max_length=255)
    address=forms.CharField(label='Address',max_length=255)
    phone=forms.CharField(label='Phone',max_length=10)
    sos_contact=forms.CharField(label='Sos Contact',max_length=10)
    gender=forms.CharField(label='Gender',widget=forms.RadioSelect(choices=GENDER))