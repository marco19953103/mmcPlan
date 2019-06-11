from rest_framework import serializers
from jobs.models import Job, JobApplicant


class JobSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=False)

    class Meta:
        model = Job
        exclude = ['header_image']
