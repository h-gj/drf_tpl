from django.http import JsonResponse
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    exception_handler(exc, context)

    # Order matters, ValidationError subclass APIException, so it should be placed above APIException handling.
    if isinstance(exc, ValidationError):
        friendly_msg = ''
        for f_name, f_err_msg in exc.detail.items():
            msg = ', '.join(f_err_msg)
            friendly_msg += (
                msg
                .replace('This field', f_name)
                .replace('This value', 'The value of ' + f_name)
                .replace('this field', f_name)
                .replace('this value', 'value of' + f_name)
            )
        return JsonResponse({'code': 40000, 'message': friendly_msg, 'data': None})

    elif isinstance(exc, APIException):
        return JsonResponse({'code': exc.get_codes(), 'message': exc.detail, 'data': None})

    else:
        return JsonResponse({'code': 50000, 'message': exc.__str__(), 'data': None})
