from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Employee(User):
    profile_image = models.ImageField(upload_to='employees/')
    hour_rate = models.DecimalField(decimal_places=2, max_digits=4, default=0.00)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class EmployeePosition(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    position = models.ForeignKey('jobs.Position', on_delete=models.CASCADE)
    hour_rate = models.DecimalField(decimal_places=2, max_digits=4, default=0.00)

    def __str__(self):
        return self.position.description

    class Meta:
        unique_together = ('employee', 'position')
