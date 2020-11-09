from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins
from rest_framework.viewsets import GenericViewSet
from users.models import User
from .models import Organization, Staff, Team
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .database_helper_functions import DBHelper
from .validators import ECoachValidators


from .serializers import ECoachUserSerializer, TeamMemberSerializer, TeamStaffMemberSerializer, TeamDetailSerializer, \
    TeamGetSerializer, OrganizationGetSerializer, OrganizationPostSerializer, TeamPostSerializer, \
    TeamMemberGetSerializer


class ECoachUserAPIView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        GenericViewSet):

    serializer_class = ECoachUserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


class OrganizationAPIView(APIView):

    def get(self, *args, **kwargs):
        organizations = []
        staff_instances = Staff.objects.filter(user=self.request.user)
        for staff_instance in staff_instances:
            if staff_instance.organization is not None:
                organizations.append(staffi_instance.organization)
        serializer = OrganizationGetSerialzer(organizations, many=True, context={"request": self.request})
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        user_data = self.request.data
        serializer = OrganizationPostSerializer(data=user_data)
        is_valid = serializer.is_valid()
        print(serializer.validated_data)
        if not is_valid:
            return Response({'detail': 'input not valid'}, status=400)
        new_organization = serializer.save(owner=self.request.user)
        new_staff_object = Staff(user=self.request.user, organization=new_organization)
        new_staff_object.save()
        get_serializer = OrganizationGetSerializer(new_organization, context={'request': self.request})
        return Response(get_serializer.data)


class OrganizationDetailAPIView(APIView):
    """APIView for allowing user to see information about Organisations they are signed up to"""

    def get(self, *args, **kwargs):
        url_argument = self.kwargs['name']

        try:
            current_organisation = Organization.objects.get(slug=url_argument)
        except Organization.DoesNotExist:
            raise Http404

        serializer = OrganizationGetSerializer(current_organisation, context={'request': self.request})
        return Response(serializer.data)

    def patch(self, *args, **kwargs):
        url_argument = self.kwargs['name']
        print(url_argument)
        user_data = self.request.data
        try:
            current_organisation = Organization.objects.get(slug=url_argument)
        except Organization.DoesNotExist:
            raise Http404

        serializer = OrganizationPostSerializer(current_organisation, data=user_data)
        is_valid = serializer.is_valid()
        print(serializer.validated_data)
        if not is_valid:
            return Response({'detail': 'input not valid'}, status=400)
        new_organization = serializer.save()
        get_serializer = OrganizationGetSerializer(new_organization, context={'request': self.request})
        return Response(get_serializer.data)

    def delete(self, *args, **kwargs):
        url_argument = self.kwargs['name']
        user = self.request.user
        try:
            organization = Organization.objects.get(slug=name)
        except Organization.DoesNotExist:
            raise Http404
        if organization.owner == user:
            organization.delete()
            return Response({'detail': 'Organization has been successfully deleted'}, status=200)
        return Response({'detail': 'Action Forbidden'}, status=403)




class TeamAPIView(APIView):
    """TeamAPIView
    get: shows list of teams user is a member of"""

    def get(self, *args, **kwargs):
        teams = DBHelper.user_to_teams_staff(self.request.user)
        serializer = TeamGetSerializer(teams, context={"request": self.request}, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        user_data = self.request.data
        serializer = TeamPostSerializer(data=user_data)
        is_valid = serializer.is_valid()
        print(serializer.validated_data)
        if not is_valid:
            return Response({'detail': 'input not valid'}, status=400)
        new_team = serializer.save()
        get_serializer = TeamGetSerializer(new_team, context={'request': self.request})
        return Response(get_serializer.data)



class TeamDetailAPIView(APIView):
    """API view to allow user to access important information about team"""

    def get(self, *args, **kwargs):
        url_parameter = self.kwargs['name']
        try:
            team = Team.objects.get(slug=url_parameter)
        except Team.DoesNotExist:
            raise Http404
        serializer = TeamDetailSerializer(team, context={"request": self.request})
        return Response(serializer.data)

    def patch(self, *args, **kwargs):
        url_parameter = self.kwargs['name']
        try:
            team = Team.objects.get(slug=url_parameter)
        except Team.DoesNotExist:
            raise Http404
        user_data = self.request.data
        serializer = TeamPostSerializer(team, data=user_data)
        is_valid = serializer.is_valid()
        print(serializer.validated_data)
        if not is_valid:
            return Response({'detail': 'input not valid'}, status=400)
        new_team = serializer.save()
        get_serializer = TeamGetSerializer(new_team, context={'request': self.request})
        return Response(get_serializer.data)

    def delete(self):
        url_argument = self.kwargs['name']
        user = self.request.user
        try:
            team = Team.objects.get(slug=url_argument)
        except Team.DoesNotExist:
            raise Http404
        if team.organization.owner == user:
            team.delete()
            return Response({'detail': 'Team has been successfully deleted'}, status=200)
        return Response({'detail': 'Action Forbidden'}, status=403)


class TeamMemberAPIView(APIView):
    """APIView to get the information from an individual member """

    def get(self, *args, **kwargs):
        user_id = self.kwargs['id']

        try:
            member = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404

        if ECoachValidators.team_member_validator(member, self.request.user):
            serializer =TeamMemberGetSerializer(member, context={'request': self.request})
            return Response(serializer.data)

        return Response({'detail': 'Access Forbidden'}, status=403)
