from django.shortcuts import render
from django.http import HttpResponse 
from .forms import EventRegistration,ParticipantRegistration,Dashboard
from .models import Event, Participant
from django.core.mail import send_mail
import os
from twilio.rest import Client

# Create your views here.

def start_home(request):
     return render(request, 'index.html')

def showE_r(request):
     if request.method == 'POST':
          fm = EventRegistration(request.POST)
          if fm.is_valid():
               en = fm.cleaned_data['E_name']
               de = fm.cleaned_data['Description']
               lo = fm.cleaned_data['Location']
               sd = fm.cleaned_data['s_date']
               ed = fm.cleaned_data['e_date']
               rd = fm.cleaned_data['R_d_date']
               he = fm.cleaned_data['H_email']
               hp = fm.cleaned_data['H_password']

               data = [ he ]

               reg = Event(E_name=en,Description=de,Location=lo,s_date=sd,e_date=ed,R_d_date=rd,H_email=he,H_password=hp)
               reg.save() 
               message = '''

               Thank you for registration your event with us.

               Event Name: {}
               Event ID: {}

               you can now review the participation in your event through our portal.
               
               Regards,
               Emanage web app.
               '''.format( en , reg.id )
               send_mail("Event Registration Successful",message,'',data,fail_silently=False)
               fm = EventRegistration() 
     else:
          fm = EventRegistration()
          
     return render(request, 'Event_registration.html', {'form':fm})

def showP_r(request):
     if request.method == 'POST':
          fm = ParticipantRegistration(request.POST)
          if fm.is_valid():
               n = fm.cleaned_data['name']
               cn = fm.cleaned_data['c_no']
               em = fm.cleaned_data['email']
               e = fm.cleaned_data['Event']
               r = fm.cleaned_data['R_type']
               np = fm.cleaned_data['N_people']
               reg = Participant(name=n,c_no=cn,email=em,Event=e,R_type=r,N_people=np)
               reg.save()

               account_sid = 'AC3f5d5d240cc7cbe2dbfdbc300f0f13a5'
               auth_token = '50bd8d9fbc2dc8092a345524708e114f'
               client = Client(account_sid, auth_token)

               message = client.messages \
                               .create(
                                   body=f"Participant ID : {reg.id} \nEvent name : {reg.Event} \nLocation : {reg.Event.Location} \n Date : {reg.Event.s_date}-{reg.Event.e_date}\nParticipation type : {reg.R_type} \nNo of people : {reg.N_people}",
                                   from_='+17407593742',
                                   to = '+91'+str(reg.c_no)
                               )

               fm = ParticipantRegistration()

     else:
          fm = ParticipantRegistration()
          
     return render(request, 'Participant_registration.html', {'form1':fm})

def showE_d(request):
     if request.method == 'POST':
          fm = Dashboard(request.POST)
          if fm.is_valid():
               en = fm.cleaned_data['E_name']
               de = fm.cleaned_data['Description']
               lo = fm.cleaned_data['Location']
               sd = fm.cleaned_data['s_date']
               ed = fm.cleaned_data['e_date']
               rd = fm.cleaned_data['R_d_date']
               he = fm.cleaned_data['H_email']
               hp = fm.cleaned_data['H_password']

     else:
          fm = Dashboard()
          
     return render(request, 'Event_dashboard.html', {'form2':fm})

