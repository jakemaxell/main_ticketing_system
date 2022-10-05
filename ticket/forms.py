from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'title', 'type', 'description')
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control my-1'}),
            'title': forms.TextInput(attrs = {'class': 'form-control my-1'}),
            'type': forms.TextInput(attrs = {'class': 'form-control my-1'}),
            'description': forms.TextInput(attrs = {'class': 'form-control my-1'})
        }
        labels = {
            'name': 'Please enter your name',
            'title': 'Ticket Title',
            'type': 'Type of IT issue you are experiencing',
            'description': "Description"
        }