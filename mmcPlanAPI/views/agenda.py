from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from mmcPlanAPI.serializers.agenda import AgendaSerializer, AgendaItem

from datetime import date


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

    def create(self, request):
        call = request.data
        token = get_object_or_404(Token, key=call.pop('userToken'))
        if call['date'] is None:
            call['date'] = date.today()
        call['employee_id'] = token.user.id
        try:
            AgendaItem.objects.create(**call)
            return Response({'message': 'Item is aangemaakt!', 'error': False})
        except Exception as e:
            return Response({'message' : str(e), 'error': True})

