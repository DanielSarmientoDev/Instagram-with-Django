#import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#import User
from django.contrib.auth.models import User
#import models
from django.contrib import admin

from users.models import Profile
# Register your models here.
#Import Posts
from posts.models import Post


@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    #Profile Admin
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user',)
    list_editable = ('phone_number', 'website', 'picture')
    
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'

    )
    
    list_filter = (
         'user__is_active',
         'user__is_staff',
         'create',
         'modified',
         )
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('create', 'modified'),),
        })
    )

    readonly_fields = ('create', 'modified','user')

class ProfileInline(admin.StackedInline):
    #Profile in-line admin for users

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    #add profiles admin to base user admin.

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'

    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display=('pk', 'title','photo', 'created', 'modified')
    list_display_links=('pk', 'created')
    search_fields = (
        'created',
        'modified'
    )
    list_filter = (
        'title',
        'created'
    )

    #Evitar que ciertos campos sean editables
    readonly_fields = ('created', 'modified')