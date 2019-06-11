from django.db import models
from customers.models import Customer
from employees.models import Employee


# Create your models here.
class Job(models.Model):
    header_image = models.ImageField(upload_to="job_images/", blank=True)
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class JobApplicant(models.Model):
    STATUSES = (
        (0, 'pending'),
        (1, 'approved'),
        (2, 'denied')
    )
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    status = models.SmallIntegerField(choices=STATUSES, default=0)

    def __str__(self):
        return self.employee.get_full_name()

    class Meta:
        unique_together = ('job', 'employee')
