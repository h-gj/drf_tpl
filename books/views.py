from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from books.constructors import AuthorListKeyConstructor
from books.filters import AuthorFilter
from books.models import Author
from books.serializers import AuthorSerializer


class AuthorViewSet(CacheResponseMixin,
                    ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
    list_cache_key_func = AuthorListKeyConstructor()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = AuthorFilter

    @action(methods=['get'], detail=False)
    def with_little_fields(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
