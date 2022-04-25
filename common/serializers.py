from collections import OrderedDict

from rest_framework import serializers

from common.utils import deep_get, deep_getattr


class BaseModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    modified_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')


class ActionFieldsModelSerializer(BaseModelSerializer):
    # TODO: Do not return base model serializer fields automatically.
    def __init__(self, *args, **kwargs):
        self.exclude = deep_get(kwargs, ['context', 'exclude'], [])
        self.include = deep_get(kwargs, ['context', 'include'], [])
        super().__init__(*args, **kwargs)

    def get_fields(self):
        """
        Override this method to support `action_fields` on serializer Meta attr.
        """
        fields = super().get_fields()
        view = self.context.get('view')

        action_fields = deep_getattr(self, 'Meta.action_fields')
        if action_fields:
            # exclude = action_fields.get(view.action, {}).get('exclude', [])
            # include = action_fields.get(view.action, {}).get('fields', [])
            exclude = self.exclude or deep_get(action_fields, [getattr(view, 'action', None), 'exclude'], [])
            include = self.include or deep_get(action_fields, [getattr(view, 'action', None), 'fields'], [])

            field_names = list(fields.keys())
            for field_name in exclude:
                if field_name not in field_names:
                    raise ValueError('Unrecognized field: %s' % field_name)

            for field_name in include:
                if field_name not in field_names:
                    raise ValueError('Unrecognized field: %s' % field_name)

            if include:
                fields = OrderedDict(
                    {field_name: fields.get(field_name)
                     for field_name in include
                     if fields.get(field_name)}
                )

            if exclude:
                fields = OrderedDict(
                    {field_name: fields.get(field_name)
                     for field_name in fields
                     if field_name not in exclude}
                )

        return fields
