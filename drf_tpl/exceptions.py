from django.http import JsonResponse
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    exception_handler(exc, context)
    if isinstance(exc, APIException):
        return JsonResponse({'code': exc.get_codes(), 'message': exc.detail, 'data': None})
    else:
        return JsonResponse({'code': 50000, 'message': exc.__str__(), 'data': None})
