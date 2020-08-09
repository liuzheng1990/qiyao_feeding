from rest_framework import serializers
from ..models import QiyaoEvent

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = QiyaoEvent
        fields = ["event_type", "time", "int_param", "str_param"]