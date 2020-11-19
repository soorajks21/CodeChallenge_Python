from rest_framework import serializers


class RandomAPISerializer(serializers.Serializer):
    value = serializers.CharField()
    
