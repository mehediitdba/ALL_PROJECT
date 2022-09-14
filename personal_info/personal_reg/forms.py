from django import forms
from .models import Personal

class PersonalForm(forms.ModelForm):

    class Meta:
        model = Personal
        fields = ('fullname','mobile','per_code','position')
        labels={
            'fullname':'Full Name :',
            'mobile':'Mobile No :',
            'per_code':'Personal Code :',
            'position':'Position :'
        }
    
    def __init__(self, *args, **kwargs):
        super(PersonalForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['per_code'].required=False