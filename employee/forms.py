from django import forms
from .models import SuperVisors,labour

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = SuperVisors
        fields = '__all__'

class labourForm(forms.ModelForm):
    class Meta:
        model = labour
        fields = '__all__'

class SupervisorUpdateForm(forms.ModelForm):
    class Meta:
        model = SuperVisors
        fields = ('project','name','mobile_number','alter_number','address','aadhar_number',
        'pan_number','highest_qual','tech_certificate_name','UAN_number','is_employee')