from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import SessionEntry, GeneralDayEntry, CompetitionEntry, Result, Goal, Objective
from .serializers import SessionEntrySerializer, GeneralDayEntrySerializer, CompetitionEntrySerializer, \
    ResultSerializer, GoalSerializer, ObjectiveSerializer


class SessionEntryViewSet(viewsets.ModelViewSet):

    serializer_class = SessionEntrySerializer

    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return SessionEntry.objects.filter(author=self.request.user)

class GeneralDayEntryViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GeneralDayEntrySerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):

        return GeneralDayEntry.objects.filter(author=self.request.user)


class CompetitionEntryViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CompetitionEntrySerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):

        return CompetitionEntry.objects.filter(author=self.request.user)


class ResultViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ResultSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Result.objects.filter(author=self.request.user)


class GoalViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GoalSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Goal.objects.filter(author=self.request.user)


class ObjectiveViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ObjectiveSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Objective.objects.filter(author=self.request.user)