from django.contrib import admin
from .models import Event,Participant
# Register your models here.

@admin.register(Event)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','E_name','Description','Location','s_date','e_date','R_d_date','H_email','H_password')

@admin.register(Participant)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','c_no','email','Event','R_type','N_people')

