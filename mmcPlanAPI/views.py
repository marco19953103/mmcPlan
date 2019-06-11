from rest_framework import viewsets
from mmcPlanAPI.serializers.jobs import JobSerializer, Job


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
