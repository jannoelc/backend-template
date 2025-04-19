from django.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView

# API URLS
urlpatterns = [
    # API base url
    path("api/", include("config.api_router")),

    # Auth
    path("api/auth/", include("allauth.headless.urls")),

    # Swagger
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

