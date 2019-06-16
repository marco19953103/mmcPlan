from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from mmcPlanAPI.serializers.agenda import AgendaSerializer, AgendaItem


class AgendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AgendaItem.objects.all()
    serializer_class = AgendaSerializer
