from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, EmployeePosition
from django.utils.safestring import mark_safe
# Register your models here.


class PositionsInline(admin.TabularInline):
    model = EmployeePosition
    extra = 0


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    fields = ('headshot_image', 'profile_image', 'username', 'password', 'email', 'first_name', 'last_name', 'hour_rate')
    fieldsets = None
    inlines = [PositionsInline]
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.profile_image.url,
            width=obj.profile_image.width,
            height=obj.profile_image.height,
            )
    )
