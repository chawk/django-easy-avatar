from easy_avatar.models import Easy_Avatar
from django.contrib import admin
    
class Easy_AvatarAdmin(admin.ModelAdmin):
    list_display = ('user',)

    def name(self, instance):
        return instance.user.username

admin.site.register(Easy_Avatar, Easy_AvatarAdmin)