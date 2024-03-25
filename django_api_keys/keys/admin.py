from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import KeysUser

# Register your models here.

from .models import InternalKey, ExternalKey

# Register your models here.

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = KeysUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('external_keys',)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('external_keys',)}),
    )
 
 
admin.site.register(InternalKey)
admin.site.register(ExternalKey)
admin.site.register(KeysUser, UserAdmin)