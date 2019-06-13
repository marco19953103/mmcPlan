from django.db import models
from customers.models import Customer
from employees.models import Employee
from django.utils import timezone


# Create your models here.
class Job(models.Model):
    header_image = models.ImageField(upload_to="job_images/", blank=True, default='default.png')
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    max_applicants = models.PositiveIntegerField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Position(models.Model):
    description = models.CharField(max_length=128)
    min_wage = models.DecimalField(decimal_places=2, default=0.00, blank=True, max_digits=10)

    def __str__(self):
        return self.description


class JobApplicant(models.Model):
    STATUSES = (
        (0, 'pending'),
        (1, 'approved'),
        (2, 'denied')
    )
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)
    status = models.SmallIntegerField(choices=STATUSES, default=0)

    def __str__(self):
        return self.employee.get_full_name()

    class Meta:
        unique_together = ('job', 'employee')


class JobPositions(models.Model):
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, blank=True)

    class Meta:
        unique_together = ('job', 'position')
