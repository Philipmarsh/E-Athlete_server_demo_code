import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    GENDERS = (('Male', 'Male'),
               ('Female', 'Female'))
    coach_name = models.CharField(null=True, max_length=40, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(blank=True, default='anon-profile-picture.png')
    sex = models.CharField(max_length=10, choices=GENDERS, blank=True, null=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank= True)
    sport = models.CharField(null=True, max_length=130, blank=True)
    short_term_goal = models.CharField(max_length=400, null=True, blank=True)
    medium_term_goal = models.CharField(max_length=400, null=True, blank=True)
    long_term_goal = models.CharField(max_length=400, null=True, blank=True)



class FCMToken(models.Model):
    #TODO need to check whether user is still logged into the device
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token = models.CharField(max_length=500, null=False, blank=False)
    latest_login = models.DateTimeField(auto_now=True)

