from email import message
from os import name
from tkinter.tix import Form
from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
