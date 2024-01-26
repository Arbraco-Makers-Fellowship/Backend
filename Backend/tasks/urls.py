# tasks/urls.py
from django.urls import path
from .views import TaskListCreateView, TaskDeleteView, TaskUpdateStatusView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('list/', TaskListCreateView.as_view(), name='task-list-create'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('update-status/<int:pk>/', TaskUpdateStatusView.as_view(), name='task-update-status'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
