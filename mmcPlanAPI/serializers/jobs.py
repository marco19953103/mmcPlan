from rest_framework import serializers
from jobs.models import Job, JobApplicant, JobPositions


class JobPositionsSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField(many=False)

    class Meta:
        model = JobPositions
        fields = ('id', 'position', 'quantity')


class JobApplicantSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(many=False)
    position = serializers.StringRelatedField(many=False)

    class Meta:
        model = JobApplicant
        fields = ('id', 'employee', 'position', 'status')


class JobSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=False)
    jobapplicant_set = JobApplicantSerializer(many=True, read_only=True)
    jobpositions_set = JobPositionsSerializer(many=True, read_only=True)
    start_date = serializers.DateField(format="%d/%m/%Y", input_formats=["%d-%m-%Y", "%Y-%m-%d"])
    start_time = serializers.TimeField(format="%H:%M")
    end_date = serializers.DateField(format="%d/%m/%Y", input_formats=["%d-%m-%Y", "%Y-%m-%d"])
    end_time = serializers.TimeField(format="%H:%M")

    class Meta:
        model = Job
        fields = '__all__'
