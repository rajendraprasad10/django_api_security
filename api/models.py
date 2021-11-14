from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    GENDER_CHOICES= (
        ('M', 'Male'),
        ('F', 'Female')
    )
    title = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES)
    create_by = models.ForeignKey(User, related_name='created_by' ,on_delete=models.PROTECT, default=1)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,)
    
