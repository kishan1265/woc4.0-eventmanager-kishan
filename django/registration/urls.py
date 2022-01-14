from django.urls import path
from . import views

urlpatterns = [ 

        path('',views.start_home),
        path('home_page/',views.start_home),
        path('Event_registration/',views.showE_r),
        path('Participant_registration/',views.showP_r),
        path('Event_dashboard/',views.showE_d)
]