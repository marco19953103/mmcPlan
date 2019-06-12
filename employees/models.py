from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Employee(User):
    profile_image = models.ImageField(upload_to='employees/')

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


