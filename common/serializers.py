from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    modified_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
