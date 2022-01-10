from django.core import validators
from django import forms
from django.forms import fields, widgets
from .models import Event,Participant,Dashboardm

class EventRegistration(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['E_name','Description','Location','s_date','e_date','R_d_date','H_email','H_password']
        labels = {'E_name':'Event name','s_date':'From','e_date':'To','R_d_date':'Registration Deadline','H_email':'Host E-mail','H_password':'Host password'}
        help_text = {'E_name':'Enter Event name','Description':'Description here...','Location':'Enter location','s_date':'dd-mm-yyyy','e_date':'dd-mm-yyyy','R_d_date':'dd-mm-yyyy','H_email':'Enter email','H_password':'Enter password'}
        error_messages = {'E_name':{'required':'please Enter event name'}}
        widgets = {'H_password':forms.PasswordInput(attrs={'placeholder':'Enter host password'}),
                   'E_name':forms.TextInput(attrs={'placeholder':'Enter Event name'}),
                   'Description':forms.Textarea(attrs={'placeholder':'Enter description here...'}),
                   'Location':forms.TextInput(attrs={'placeholder':'Enter Location '}),
                   's_date':forms.DateInput(attrs={'placeholder':'dd-mm-yyyy','type':'datetime-local'}),
                   'e_date':forms.DateInput(attrs={'placeholder':'dd-mm-yyyy','type':'datetime-local'}),
                   'R_d_date':forms.DateInput(attrs={'placeholder':'dd-mm-yyyy','type':'datetime-local'}),
                   'H_email':forms.EmailInput(attrs={'placeholder':'Enter e-mail id'}),}

class ParticipantRegistration(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name','c_no','email','Event','R_type','N_people']
        labels = {'name':'Name','c_no':'Contact No','email':'Email ID','Event':'Event','R_type':'Registration-Type','N_people':'No. of People'}
        widgets = {'name':forms.TextInput(attrs={'placeholder':'Enter your Name'}),
                   'c_no':forms.TextInput(attrs={'placeholder':'Enter your contact no'}),
                   'email':forms.EmailInput(attrs={'placeholder':'Enter e-mail id'}),
                   'N_people':forms.TextInput(attrs={'type':'number'})}

class Dashboard(forms.ModelForm):
    class Meta:
        model = Dashboardm
        fields = ['E_id','H_password']
        labels = {'E_id':'Event-ID','H_password':'Host-Password'}
        widgets = {'E_id':forms.TextInput(attrs={'placeholder':'Enter Event ID'}),
                   'H_password':forms.PasswordInput(attrs={'placeholder':'Enter Host password'}),}

