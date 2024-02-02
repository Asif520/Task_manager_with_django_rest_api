from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
        
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True,null=True)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS = []


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=20, choices=[('Low','low'), ('Medium','medium'), ('High','high')])
    is_complete = models.CharField(max_length=20, choices=[('Yes','yes'),('No','no')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    photo = models.ImageField(null=True, upload_to='images',blank=True)

    
    class Meta:
        ordering = ['-updated_at','-created_at']


# Create your models here.
