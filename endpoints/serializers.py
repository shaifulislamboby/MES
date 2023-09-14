import datetime

from rest_framework import serializers


class MaintenanceSerializer(serializers.Serializer):
    ConversationId = serializers.CharField(max_length=572, required=True)
    MessageId = serializers.IntegerField(required=True)
    MachineName = serializers.CharField(max_length=256, required=True)
    MaintenanceThreshold = serializers.IntegerField(required=True)
    PlannedMaintenanceStart = serializers.CharField(default=datetime.datetime.now())
    PlannedMaintenanceEnd = serializers.CharField(default=datetime.datetime.now())
