# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import SessionEntry, GeneralDayEntry, CompetitionEntry, Result, Goal, Objective


class SessionEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = SessionEntry
        fields = ['title', 'date', 'time', 'intensity', 'performance', 'feeling', 'target', 'reflections', 'id']


class GeneralDayEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralDayEntry
        fields = ['rested', 'date', 'nutrition', 'concentration', 'reflections', 'id']


class CompetitionEntrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CompetitionEntry
        fields = ['date', 'name', 'address', 'start_time', 'id']


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ['name', 'date', 'position', 'reflections', 'id']


class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = ['content', 'deadline', 'set_on_date', 'goal_type', 'achieved', 'id']


class ObjectiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Objective
        fields = ['start_date', 'end_date', 'is_finished', 'objective_type', 'average', 'hours_of_work', 'id']
