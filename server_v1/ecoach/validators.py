from .models import Team, Staff, Member


class ECoachValidators:
    # TODO: rewrite this method so it doesnt suck as much
    @staticmethod
    def team_member_validator(member, staff_member):
        is_valid = False
        member_objects = Member.objects.filter(user=member)
        teams_with_user = []
        for member_object in member_objects:
            teams_with_user.append(member_object.team)
        if teams_with_user is not None:
            for team in teams_with_user:
                staff_objects = list(Staff.objects.filter(team=team)) + list(Staff.objects.filter(organization=team.organization))
                for staff_object in staff_objects:
                    if staff_object.user == staff_member:
                        is_valid = True
                        break
                if is_valid:
                    break
        return is_valid
