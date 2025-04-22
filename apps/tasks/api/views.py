from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.tasks.models import Task
from .serializers import TaskSerializer
from .pagination import CustomPageNumberPagination

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status']
    ordering_fields = ['created_at', 'updated_at', 'status']
    ordering = ['-created_at']
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(created_by=user)
        ordering = self.request.query_params.get('ordering', None)
        if ordering in ['created_at', 'updated_at', 'status']:
            return queryset.order_by(ordering)
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['partial'] = self.request.method == 'PATCH'
        serializer = serializer_class(*args, **kwargs)
        if self.request.method == 'PATCH':
            serializer.fields.pop('name', None)
            serializer.fields.pop('description', None)
        return serializer