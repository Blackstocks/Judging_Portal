from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import customUser, participant

class CustomUserAdmin(UserAdmin):
    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[0] = (None, {'fields': ('username', 'password', 'is_judge', 'is_participant')})
    UserAdmin.fieldsets = tuple(fieldsets)

    list_filter = list(UserAdmin.list_filter)
    list_filter.append('is_judge')
    UserAdmin.list_filter = tuple(list_filter)

    list_display = ('username','first_name', 'last_name', 'is_judge', 'email')


admin.site.register(customUser, CustomUserAdmin)

admin.site.register(participant)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import customUser

# fields = list(UserAdmin.fieldsets)
# fields[0] = (None, {'fields': ('username', 'password', 'is_judge', 'is_particpant')})
# UserAdmin.fieldsets = tuple(fields)
# filter = list(UserAdmin.list_filter)
# filter[3] = (None, {'Filter ': ('is_judge', 'is_participant')})
# UserAdmin.list_filter = tuple(filter)

# admin.site.register(customUser, UserAdmin)