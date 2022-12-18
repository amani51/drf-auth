from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_fieldsets=((
        'Basic Information',{
            'fields':('username','email','password1', 'password2')
        }
    ),(
        'Personal Information',{
            'fields':('first_name','last_name','phone_number')
        }
    ),

    )

admin.site.register(CustomUser,CustomUserAdmin)