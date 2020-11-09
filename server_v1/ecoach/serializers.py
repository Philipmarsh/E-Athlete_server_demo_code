from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from users.models import User
from .models import Team, Staff, Member, Organization
from .database_helper_functions import DBHelper
from diary.serializers import GeneralDayEntrySerializer, SessionEntrySerializer, CompetitionEntrySerializer, \
    ResultSerializer
from diary.models import GeneralDayEntry, SessionEntry, CompetitionEntry, Result





class ECoachUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'coach_name', 'id', 'date_of_birth', 'profile_photo', 'sex']

    profile_photo = Base64ImageField(use_url=True)


# TODO: create serializer for organisation info api

class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializer to get information about members in a team"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile_photo', 'id']

    def get_profile_photo(self, user):
        request = self.context.get('request')
        photo_url = user.profile_photo.url
        return request.build_absolute_uri(photo_url)

    profile_photo = serializers.SerializerMethodField(read_only=True)


class TeamStaffMemberSerializer(serializers.Serializer):
    """Serializer to get information about staff in a team"""

    def get_profile_photo(self, staff):
        request = self.context.get('request')
        return request.build_absolute_uri(staff.user.profile_photo.url)

    def get_first_name(self, staff):
        return staff.user.first_name

    def get_last_name(self, staff):
        return staff.user.last_name

    def get_id(self, staff):
        return staff.user.id

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()
    profile_photo = serializers.SerializerMethodField()
    role = serializers.CharField(max_length=100, source='title')


class TeamDetailSerializer(serializers.ModelSerializer):
    """Serializer for team"""

    class Meta:
        model = Team
        fields = ['name', 'user_role', 'slug', 'description', 'organization_name', 'organization_slug',
                  'number_of_members', 'max_members', 'address', 'members', 'staff']

    def get_members(self, team):
        members = DBHelper.team_to_members(team)
        return TeamMemberSerializer(members, many=True, context=self.context).data

    def get_staff(self, team):
        staff = DBHelper.team_to_staff(team)
        return TeamStaffMemberSerializer(staff, many=True, context=self.context).data

    def get_organization_slug(self, team):
        return team.organization.slug

    def get_organization_name(self, team):
        return team.organization.name

    def get_user_role(self, team):
        request = self.context.get('request')
        staff_objects = Staff.objects.filter(team=team)
        for staff_object in staff_objects:
            if staff_object.user == request.user:
                return staff_object.title

    def get_number_of_members(self, team):
        members = Member.objects.filter(team=team)
        if members is None:
            return 0
        return len(members)

    organization_name = serializers.SerializerMethodField()
    organization_slug = serializers.SerializerMethodField()
    number_of_members = serializers.SerializerMethodField()
    user_role = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()
    staff = serializers.SerializerMethodField()


class TeamGetSerializer(serializers.ModelSerializer):

    class Meta:
        model= Team
        fields = ['user_role', 'name', 'slug', 'description', 'organization_name', 'organization_slug',
                  'number_of_members', 'max_members', 'address']

    def get_user_role(self, team):
        request = self.context.get('request')
        staff_objects = Staff.objects.filter(team=team)
        for staff_object in staff_objects:
            if staff_object.user == request.user:
                return staff_object.title

    def get_organization_name(self, team):
        return team.organization.name

    def get_organization_slug(self, team):
        return team.organization.slug

    def get_number_of_members(self, team):
        members = Member.objects.filter(team=team)
        if members is None:
            return 0
        return len(members)

    user_role = serializers.SerializerMethodField()
    organization_name = serializers.SerializerMethodField()
    organization_slug = serializers.SerializerMethodField()
    number_of_members = serializers.SerializerMethodField()


class TeamPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['name', 'organization_slug', 'description', 'address', 'slug']

    organization_slug = serializers.SlugField()

    def create(self, validated_data):
        validated_data['organization'] = Organization.objects.get(slug=validated_data['organization_slug'])
        del validated_data['organization_slug']
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        try:
            validated_data['organization'] = Organization.objects.get(slug=validated_data['organization_slug'])
            del validated_data['organization_slug']
        except:
            print('cool beans')
        instance.name = validated_data.get('name', instance.name)
        instance.organization = validated_data.get('organization', instance.organization)
        instance.description = validated_data.get('description', instance.description)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance


class OrganizationGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ['logo', 'name', 'created', 'description', 'number_of_teams', 'slug', 'max_teams', 'staff', 'teams']

    def get_teams(self, organization):
        teams = Team.objects.filter(organization=organization)
        return TeamsInOrganizationSerializer(teams, many=True).data

    def get_staff(self, team):
        staff = DBHelper.organization_to_staff(team)
        return TeamStaffMemberSerializer(staff, many=True, context=self.context).data

    def get_logo(self, organization):
        request = self.context.get('request')
        return request.build_absolute_uri(organization.logo.url)

    def get_number_of_teams(self, organization):
        teams = Team.objects.filter(organization=organization)
        if teams is None:
            return 0
        return len(teams)

    teams = serializers.SerializerMethodField()
    staff = serializers.SerializerMethodField()
    logo = serializers.SerializerMethodField()
    number_of_teams = serializers.SerializerMethodField()


class OrganizationPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ['name', 'description', 'address', 'slug']

    def create(self, validated_data):
        return Organization.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.address = validated_data.get('address', instance.description)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance


class TeamsInOrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['name', 'number_of_members', 'max_members']

    def get_number_of_members(self, team):
        members = Member.objects.filter(team=team)
        if members is None:
            return 0
        return len(members)

    number_of_members = serializers.SerializerMethodField()


class TeamMemberGetSerializer(serializers.ModelSerializer):
    """Serializer to get the sessions, general days, results and competitions of user in a team"""

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'profile_photo', 'general_days', 'sessions', 'results', 'competitions']

    def get_general_days(self, user):
        general_days = GeneralDayEntry.objects.filter(author=user)
        return GeneralDayEntrySerializer(general_days, many=True).data

    def get_sessions(self, user):
        sessions = SessionEntry.objects.filter(author=user)
        return SessionEntrySerializer(sessions, many=True).data

    def get_results(self, user):
        results = Result.objects.filter(author=user)
        return ResultSerializer(results, many=True).data

    def get_competitions(self, user):
        competitions = CompetitionEntry.objects.filter(author=user)
        return CompetitionEntrySerializer(competitions, many=True).data

    def get_profile_photo(self, user):
        request = self.context.get('request')
        return request.build_absolute_uri(user.profile_photo.url)

    general_days = serializers.SerializerMethodField()
    sessions = serializers.SerializerMethodField()
    results = serializers.SerializerMethodField()
    competitions = serializers.SerializerMethodField()
    profile_photo = serializers.SerializerMethodField()


