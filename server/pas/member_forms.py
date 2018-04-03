from django import forms
from .models import Member


def add_attrs(placeholder='', display=True):

    attrs =  {
        'class': 'form-control',
        'placeholder': placeholder
    }
    if not display:
        attrs['style'] = 'display: none;'
    return attrs


class AddMemberForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs=add_attrs('Enter name')))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs=add_attrs('Enter email')))
    course = forms.CharField(label='Course', widget=forms.TextInput(attrs=add_attrs('Enter course')))
    card_id = forms.CharField(label='Card ID', widget=forms.TextInput(attrs=add_attrs('Enter card_id')))
    research_about = forms.CharField(label='Research about', widget=forms.TextInput(attrs=add_attrs('Enter the topics')))

    class Meta:
        model = Member
        fields = ['name', 'email', 'course', 'card_id', 'research_about']
