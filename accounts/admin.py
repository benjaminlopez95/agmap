<<<<<<< HEAD
from django.contrib import admin
from accounts.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', 'city', 'website')

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user__username')
        return queryset




admin.site.register(UserProfile, UserProfileAdmin)
=======
from django.contrib import admin
from accounts.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', 'city', 'website')

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user__username')
        return queryset




admin.site.register(UserProfile, UserProfileAdmin)
>>>>>>> e854a0e1d078f16e921a24a3e201c203befc9c4a
