from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from apps.tasks.api.views import TaskViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register(r'tasks', TaskViewSet, basename='task')

app_name = "api"
urlpatterns = router.urls
