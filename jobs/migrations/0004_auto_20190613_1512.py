# Generated by Django 2.2.2 on 2019-06-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_max_applicants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='max_applicants',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
