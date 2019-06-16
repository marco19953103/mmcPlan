from rest_framework import serializers
from agenda.models import AgendaItem


class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgendaItem
        fields = '__all__'
