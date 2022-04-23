from rest_framework_extensions.key_constructor.bits import ListSqlQueryKeyBit, QueryParamsKeyBit
from rest_framework_extensions.key_constructor.constructors import DefaultKeyConstructor

from books.keybits import AuthorUpdatedAtKeyBit


class AuthorListKeyConstructor(DefaultKeyConstructor):
    list_sql = ListSqlQueryKeyBit()
    query_params = QueryParamsKeyBit()
    updated_at = AuthorUpdatedAtKeyBit()
