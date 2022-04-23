from rest_framework import serializers

from books.models import Author
from common.serializers import BaseModelSerializer


class AuthorSerializer(BaseModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    modified_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Author
        fields = '__all__'
