from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from member.models import CustomUser


class AdminCustomUser(UserAdmin):
    UserAdmin.fieldsets[1][1]['fields'] = ('user_name', 'email', 'team_code', 'rank_code', 'user_call')
    UserAdmin.add_fieldsets += (
        ('Additional Info', {'fields': ('user_name', 'email', 'team_code', 'rank_code', 'user_call')}),
    )
    list_display = ['username', 'user_name', 'email', 'team_code', 'rank_code']
    list_display_links = ['username', 'user_name']
    list_filter = ['username', 'user_name']


admin.site.register(CustomUser, AdminCustomUser)
