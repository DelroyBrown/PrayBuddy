from rest_framework.serializers import ModelSerializer
from base.models import Room


# RETURNS ALL FIELDS FROM 'ROOM' MODEL
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
