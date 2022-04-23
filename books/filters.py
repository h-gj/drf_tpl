from django_filters.rest_framework import FilterSet, filters

from books.models import Author


class AuthorFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Author
        fields = ('name', )
