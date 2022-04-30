from django.urls import path

from common.views import fetch_task_result

urlpatterns = [
    path('fetch_task_result', fetch_task_result),
]
