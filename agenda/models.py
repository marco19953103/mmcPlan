from django.db import models
from employees.models import Employee
# Create your models here.


class AgendaItem(models.Model):
    STATUSES = (
        (0, 'free'),
        (1, 'available'),
        (2, 'busy')
    )

    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    description = models.CharField(max_length=256, null=True, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.SmallIntegerField(default=0, choices=STATUSES)

    def __str__(self):
        return '{} {} {} {}'.format(self.date, self.start_time, self.end_time, self.status)
