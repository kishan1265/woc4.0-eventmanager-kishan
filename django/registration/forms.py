from django.forms import ModelForm
from django import forms
from .models import Event,Participant
import datetime

class EventRegistration(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['E_name','Description','Location','s_date','e_date','R_d_date','H_email','H_password']
        labels = {'E_name':'Event name','s_date':'From','e_date':'To','R_d_date':'Registration Deadline','H_email':'Host E-mail','H_password':'Host password'}
        help_text = {'E_name':'Enter Event name','Description':'Description here...','Location':'Enter location','s_date':'dd-mm-yyyy','e_date':'dd-mm-yyyy','R_d_date':'dd-mm-yyyy','H_email':'Enter email','H_password':'Enter password'}
        widgets = {'H_password':forms.PasswordInput(attrs={'placeholder':'Enter host password'}),
                   'E_name':forms.TextInput(attrs={'placeholder':'Enter Event name'}),
                   'Description':forms.Textarea(attrs={'placeholder':'Enter description here...'}),
                   'Location':forms.TextInput(attrs={'placeholder':'Enter Location '}),
                   's_date':forms.DateInput(attrs={'placeholder':'dd-mm-yyyy','type':'datetime-local'}),
                   'e_date':forms.DateInput(attrs={'placeholder':'dd-mm-yyyy','type':'datetime-local'}),
                   'R_d_date':forms.DateInput(attrs={'placeholder':'dd-mm-yyyy','type':'datetime-local'}),
                   'H_email':forms.EmailInput(attrs={'placeholder':'Enter e-mail id'})}

    def clean(self):
        cleaned_data = super().clean()
        error_found = False

        Ename = cleaned_data['E_name']
        password = cleaned_data['H_password'] 
        sdate = cleaned_data['s_date']
        edate = cleaned_data['e_date'] 
        rdate = cleaned_data['R_d_date']
        email = cleaned_data['H_email']
        pdate = datetime.datetime.now()

        if len(Ename) < 4 :
            self.add_error('E_name','Enter more than or equal 4 char')
            error_found = True

        if len(email) < 11 :
            self.add_error('H_email','Enter correct email')
            error_found = True

        if len(password) <= 6 :
            self.add_error('H_password','Enter more than 6 char')
            error_found = True

        if datetime.datetime(pdate.year,pdate.month,pdate.day,pdate.hour,pdate.minute,00) > datetime.datetime(sdate.year,sdate.month,sdate.day,sdate.hour,sdate.minute,00) :
            self.add_error('s_date','event starting date is not smaller then current date and time')
            error_found = True

        if datetime.datetime(rdate.year,rdate.month,rdate.day,rdate.hour,rdate.minute,00) > datetime.datetime(sdate.year,sdate.month,sdate.day,sdate.hour,sdate.minute,00) :
            self.add_error('R_d_date','registration date is smaller than event starting date and time')
            error_found = True

        if datetime.datetime(rdate.year,rdate.month,rdate.day,rdate.hour,rdate.minute,00) < datetime.datetime(pdate.year,pdate.month,pdate.day,pdate.hour,pdate.minute,pdate.second) :
            self.add_error('R_d_date','registration Deadline is not smaller then current date and time')
            error_found = True

        if datetime.datetime(edate.year,edate.month,edate.day,edate.hour,edate.minute,00) < datetime.datetime(sdate.year,sdate.month,sdate.day,sdate.hour,sdate.minute,00) :
            self.add_error('e_date','enter valid date because event finish before starting')
            error_found = True

        if error_found:
            raise forms.ValidationError(' ')


class ParticipantRegistration(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name','c_no','email','Event','R_type','N_people']
        labels = {'name':'Name','c_no':'Contact No','email':'Email ID','Event':'Event','R_type':'Registration-Type','N_people':'No. of People'}
        widgets = {'name':forms.TextInput(attrs={'placeholder':'Enter your Name'}),
                   'c_no':forms.TextInput(attrs={'placeholder':'Enter your contact no','type':'number'}),
                   'email':forms.EmailInput(attrs={'placeholder':'Enter e-mail id'}),
                   'N_people':forms.TextInput(attrs={'type':'number'})}

    def unique_n_check(self, cleaned_data):
            for participant in Participant.objects.all():
                if participant.c_no == cleaned_data['c_no']:
                    return False
            return True

    def unique_e_check(self, cleaned_data):
        for participant in Participant.objects.all():
            if participant.email == cleaned_data['email']:
                return False
        return True

    def clean(self):
        cleaned_data = super().clean()
        
        error_found = False

        pname = cleaned_data['name']
        c_no = cleaned_data['c_no'] 
        email = cleaned_data['email']
        np = cleaned_data['N_people']
        rt = cleaned_data['R_type']
        pdate = datetime.datetime.now()
        rdate = cleaned_data['Event'].R_d_date

        if len(pname) < 4 :
            self.add_error('name','Enter name more than or equal 4 char')
            error_found = True

        if len(email) < 11 :
            self.add_error('email','Enter correct email')
            error_found = True

        if len(c_no) < 10 or len(c_no) >10 :
            self.add_error('c_no','Enter valid contact no of 10 char')
            error_found = True

        if int(c_no) < 0 :
            self.add_error('c_no','Enter valid contact no (not negative)')
            error_found = True

        if np == 0 :
            self.add_error('N_people','number of participant is not equal to 0')
            error_found = True
        
        if np == 1 and rt != 'Individual' :
            self.add_error('R_type','if no of people is 1 than registration type is Individual')
            error_found = True

        if np != 1 and rt != 'Group' :
            self.add_error('R_type','if no of people is more than 1 ,registration type is Group')
            error_found = True

        if not self.unique_n_check(cleaned_data=cleaned_data):
            self.add_error('c_no', 'your contact number was already registered')
            error_found = True


        if not self.unique_e_check(cleaned_data=cleaned_data):
            self.add_error('email', 'your Email was already registered')
            error_found = True


        if datetime.datetime(rdate.year,rdate.month,rdate.day,rdate.hour,rdate.minute,00) < datetime.datetime(pdate.year,pdate.month,pdate.day,pdate.hour,pdate.minute,pdate.second) :
            self.add_error('Event','registration Deadline is finish take part in other event')
            error_found = True


        if error_found:
            raise forms.ValidationError('')



class Dashboard(forms.Form):

    E_id = forms.IntegerField(label='Event ID', widget=forms.TextInput(attrs={'placeholder':'Event ID', 'type':'number'}))
    H_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    
    def clean(self):
        cleaned_data = super().clean()

        e_id = Event.objects.filter(id=cleaned_data['E_id'])
        if not e_id:
            self.add_error('E_id', 'Event id is invalid')

        if e_id and e_id[0].H_password != cleaned_data['H_password']:
            self.add_error('H_password', 'event password is wrong')
