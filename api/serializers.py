from rest_framework import serializers
from .models import Box

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = [
            'id',
            'length',
            'width',
            'height', 
            'area',
            'volume',
            'createdBy',
            'lastUpdated'
        ]
