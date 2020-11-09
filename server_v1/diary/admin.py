from django.contrib import admin
from .models import SessionEntry, GeneralDayEntry, CompetitionEntry, Goal, Objective

admin.site.register(SessionEntry)
admin.site.register(GeneralDayEntry)
admin.site.register(CompetitionEntry)
admin.site.register(Goal)
admin.site.register(Objective)
