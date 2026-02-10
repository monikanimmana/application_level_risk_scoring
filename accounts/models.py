from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
        ROLE_CHOICES = (
            ('user', 'Normal User'),
            ('admin', 'Admin'),
        )
        STATUS_CHOICES = (
                ('active','Active'),
                ('restricted','Restricted'),
                ('blocked','Blocked'),         
        )
        
        role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='user')
        last_ip = models.GenericIPAddressField(null=True, blank=True)
        last_device = models.TextField(null=True, blank=True)
        risk_score = models.IntegerField(default=0)
        status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='active')

        def __str__(self):
            return self.username




