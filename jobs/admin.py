from django.contrib import admin
from .models import Job, JobApplicant
# Register your models here.


class JobApplicantInline(admin.StackedInline):
    model = JobApplicant
    extra = 0


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    inlines = [JobApplicantInline]

