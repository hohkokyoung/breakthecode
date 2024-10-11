from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator

api_version = "v2"

class SchemaGeneratorV2(OpenAPISchemaGenerator):
    def get_endpoints(self, request):
        # Get all registered endpoints
        endpoints = super().get_endpoints(request)

        # Filter endpoints to include only those with the 'api/v1/' prefix
        filtered_endpoints = {}
        for path, (view_class, methods) in endpoints.items():
            # Check if the path starts with /api/v1/
            if path.startswith(f"/api/{api_version}/"):
                filtered_endpoints[path] = (view_class, methods)

        return filtered_endpoints

schema_view = get_schema_view(
   openapi.Info(
      title="BreakTheCode System API",
      default_version=api_version,
      description="Version 2 of the BreakTheCode System API.",
      terms_of_service="",
      contact=openapi.Contact(email="kokyoung1520@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   generator_class=SchemaGeneratorV2,
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]