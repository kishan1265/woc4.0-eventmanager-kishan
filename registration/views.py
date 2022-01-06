from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def start_home(request):
     return render(request, 'index.html')

def start_Event_registration(request):
     return render(request, 'Event_registration.html')

def start_Participant_registration(request):
     return render(request, 'Participant_registration.html')

def start_Event_dashboard(request):
     return render(request, 'Event_dashboard.html')

