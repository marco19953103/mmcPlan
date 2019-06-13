from django.contrib import admin
from .models import Job, JobApplicant, Position, JobPositions
# Register your models here.


class JobApplicantInline(admin.StackedInline):
    model = JobApplicant
    extra = 0


class JobPositionsInline(admin.TabularInline):
    model = JobPositions
    extra = 0


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    inlines = [JobPositionsInline, JobApplicantInline]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
