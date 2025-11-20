from django.db import models
from accounts.models import UserProfile

# Create your models here.

class Student(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=20)
    semester = models.IntegerField()
    department = models.CharField(max_length=200)

    toughness = models.JSONField(default=dict)
    study_hours = models.JSONField(default=dict)
    sleep_hours = models.JSONField(default=dict)