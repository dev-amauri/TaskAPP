from rest_framework import serializers
from core.models import Task
class TaskSerializers (serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'subtitle',
            'description',
            'completed'
        ]
        read_only_fields = ['id']