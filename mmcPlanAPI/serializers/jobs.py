from rest_framework import serializers
from jobs.models import Job, JobApplicant


class JobApplicantSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(many=False)

    class Meta:
        model = JobApplicant
        fields = ('id', 'employee', 'status')


class JobSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=False)
    jobapplicant_set = JobApplicantSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ('id', 'title', 'description', 'customer', 'jobapplicant_set')
