from django.contrib import admin
from .models import *
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'first_name',
                    'last_name',
                    'email',
                    'is_staff'
                    )
    list_filter = (
        'is_staff',
        'is_active',
    )

    search_fields = ['last_name', 'first_name']

    readonly_fields = ('date_joined',)

    fieldsets = (
        (
            None,
            {"fields": ("cin", "username", "password")}
        ),
        (
            "Personal info",
            {
                "fields": (("first_name", "last_name"), "email")}
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(Person, PersonAdmin)