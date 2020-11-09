from .models import Team, Staff, Member, Organization


class DBHelper:

    @staticmethod
    def organization_to_teams(organization):
        """Helper function to retrieve the teams belonging to an organization"""

        teams = Team.objects.filter(organization=organization)
        teams_to_return = list(teams)
        return teams_to_return

    @staticmethod
    def team_to_members(team):
        """Helper function to retrieve the members belonging to a team"""
        members = Member.objects.filter(team=team)
        # members = list(members)
        members_to_return = []
        if members is not None:
            for member in members:
                members_to_return.append(member.user)
        return members_to_return

    @staticmethod
    def organization_to_staff(organization):
        """Helper function to retrieve the members belonging to an organization"""

        staff = Staff.objects.filter(organization=organization)
        staff_to_return = list(staff)
        return staff_to_return

    @staticmethod
    def team_to_staff(team):
        """Helper function to retrieve the members belonging to a team"""

        staff = Staff.objects.filter(team=team)
        staff_organization = Staff.objects.filter(organization=team.organization)
        staff_to_return = list(staff) + list(staff_organization)
        return staff_to_return

    @staticmethod
    def user_to_teams_staff(user):
        """Helper function to retrieve teams where user is a member of staff.
        returns a list [role, team]."""

        staff_objects = Staff.objects.filter(user=user)
        teams = []
        for staff_object in staff_objects:
            if staff_object.team is not None:
                teams.append(staff_object.team)
            if staff_object.organization is not None:
                org_teams = list(Team.objects.filter(organization=staff_object.organization))
                teams = teams + org_teams
        return teams
