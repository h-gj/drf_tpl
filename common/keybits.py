import datetime

from django.core.cache import cache
from django.utils.encoding import force_str
from rest_framework_extensions.key_constructor.bits import KeyBitBase


class UpdatedAtKeyBit(KeyBitBase):
    key = 'model_updated_at_timestamp'

    def get_data(self, **kwargs):
        value = cache.get(self.key, None)
        if not value:
            value = datetime.datetime.utcnow()
            cache.set(self.key, value=value)
        return force_str(value)
