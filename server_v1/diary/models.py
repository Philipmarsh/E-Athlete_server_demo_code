from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now


class SessionEntry(models.Model):
    """Model for Session Entry of athlete"""

    SMILEYS = (('Frustrated', 'Frustrated'),
               ('Bad', 'Bad'),
               ('Neutral', 'Neutral'),
               ('Happy', 'Happy'),
               ('Buzzing', 'Buzzing')
               )

    date = models.DateField()
    time = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(600)])
    title = models.CharField(max_length=50, default='Session')
    intensity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
    performance = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    feeling = models.CharField(choices=SMILEYS, max_length=30)
    target = models.TextField(null=True, max_length=400, blank=True)
    reflections = models.TextField(null=True, max_length=400, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.author}'

class GeneralDayEntry(models.Model):

    date = models.DateField()
    rested = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    nutrition = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    concentration = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    reflections = models.TextField(null=True, max_length=300)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.author}'


class CompetitionEntry(models.Model):

    date = models.DateField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=400, null=True)
    start_time = models.TimeField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.name}'


class Result(models.Model):

    date = models.DateField()
    name = models.CharField(max_length=50)
    position = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(20000)])
    reflections = models.TextField(max_length=500, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)


class Goal(models.Model):
    BOOL_CHOICES = (('true', 'true'),
                    ('false', 'false'),)

    GOAL_TYPES = (('Ultimate', 'Ultimate'),
                  ('Long Term', 'Long Term'),
                  ('Medium Term', 'Medium Term'),
                  ('Short Term', 'Short Term'),
                  ('Finished', 'Finished'))

    deadline = models.DateField()
    set_on_date = models.DateField()
    content = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    goal_type = models.CharField(choices=GOAL_TYPES, blank=False, null=False, max_length=40)
    achieved = models.CharField(choices=BOOL_CHOICES, blank=False, null=False, max_length=10, default='false')


class Objective(models.Model):

    BOOL_CHOICES = (('true', 'true'),
                    ('false', 'false'),)

    OBJECTIVE_CHOICES = (('Performance', 'Performance'),
                         ('Intensity', 'Intensity'),
                         ('Hours Worked', 'Hours Worked'),
                         ('Finished', 'Finished'))

    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    is_finished = models.CharField(max_length=10, choices=BOOL_CHOICES)
    objective_type = models.CharField(max_length=20, choices=OBJECTIVE_CHOICES)
    average = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True, blank=True)
    hours_of_work = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)



