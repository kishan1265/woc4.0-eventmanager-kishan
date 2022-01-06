from django.urls import path
from . import views

urlpatterns = [ 

        path('',views.start_home),
        path('home_page/',views.start_home),
        path('Event_registration/',views.start_Event_registration),
        path('Participant_registration/',views.start_Participant_registration),
        path('Event_dashboard/',views.start_Event_dashboard)
]