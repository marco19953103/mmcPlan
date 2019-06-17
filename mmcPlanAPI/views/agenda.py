from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from mmcPlanAPI.serializers.agenda import AgendaSerializer, AgendaItem


class AgendaViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def list(self, request):
        queryset = AgendaItem.objects.all()
        serializer = AgendaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        token = get_object_or_404(Token, key=pk)
        queryset = AgendaItem.objects.filter(employee_id=token.user.id)
        serializer = AgendaSerializer(queryset, many=True)
        return Response(serializer.data)
