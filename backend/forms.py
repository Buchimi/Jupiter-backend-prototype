import imp
from socket import fromshare
from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=200, default="")
    email = forms.EmailField(null=False, default="")
    year = forms.fields.IntegerField(null=True)
    transfer_student = forms.BooleanField(default=False)
    career = forms.fields.IntegerField(default=0)
    major = forms.CharField(max_length=200, default="")
