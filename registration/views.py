from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventRegistration,ParticipantRegistration,Dashboard
from .models import Event, Participant,Dashboardm

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
               reg = Event(E_name=en,Description=de,Location=lo,s_date=sd,e_date=ed,R_d_date=rd,H_email=he,H_password=hp)
               reg.save()
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

