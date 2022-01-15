from django.db import models
from django import forms
from django.forms.fields import DateTimeField

# Create your models here.

class Event(models.Model):
    E_name = models.CharField(max_length=70)
    Description = models.CharField(max_length=70)
    Location = models.CharField(max_length=70)
    s_date = models.DateTimeField()
    e_date = models.DateTimeField()
    R_d_date = models.DateTimeField()
    H_email = models.EmailField()
    H_password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.E_name

class Participant(models.Model):
    name = models.CharField(max_length=70)
    c_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    R_type = models.CharField(max_length=30,choices=(
        ('Individual', 'Individual'),
        ('Group', 'Group'),
    ))
    N_people = models.IntegerField()




