from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    pass
