from books.models import Author
from common.serializers import ActionFieldsModelSerializer


class AuthorSerializer(ActionFieldsModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        action_fields = {
            'with_little_fields': {
                'fields': ('id',),
            }
        }
