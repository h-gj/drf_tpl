import datetime

from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from books.keybits import AuthorUpdatedAtKeyBit
from books.models import Author


@receiver(post_save, sender=Author)
def handle_post_save_author(*args, **kwargs):
    cache.set(AuthorUpdatedAtKeyBit.key, datetime.datetime.utcnow())
