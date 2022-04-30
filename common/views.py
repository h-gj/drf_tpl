from celery.result import AsyncResult
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_tpl.celery import app


@api_view(['get'])
def fetch_task_result(request):
    task_id = request.GET.get('id')
    res = AsyncResult(task_id, app=app)
    return Response({'id': task_id, 'state': res.state, 'result': res.result})
