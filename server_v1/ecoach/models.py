from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=5000)
    logo = models.ImageField(blank=True, default='anon-profile-picture.png')
    address = models.TextField(max_length=400, blank=True, null=True)
    max_teams = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=3)
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    slug = models.CharField(max_length=20, unique=True)
    number_of_teams = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    # staff_members = models.ManyToManyField('Staff')


    def __str__(self):
        return self.name



class Team(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    address = models.TextField(max_length=400, blank=True, null=True)
    max_members = models.IntegerField(validators=[MinValueValidator(40), MaxValueValidator(300)], default=40)
    number_of_members = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)], default=0)
    slug = models.CharField(max_length=20, unique=True,)


    def __str__(self):
        return self.organization.name + ' ' + self.name


class Staff(models.Model):
    class Meta:
        verbose_name_plural = "Staff"
    title = models.CharField(max_length=60, default='Coach',)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Member(models.Model):

    member_type = models.CharField(max_length=60, default='Member')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)