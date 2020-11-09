from django.contrib import admin

from .models import Staff, Organization, Team, Member

admin.site.register(Staff)
admin.site.register(Organization)
admin.site.register(Team)
admin.site.register(Member)
