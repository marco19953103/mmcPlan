from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(User):

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
