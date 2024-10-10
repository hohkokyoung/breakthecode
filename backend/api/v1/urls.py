from django.contrib import admin
from django.urls import path, include

urls = [
    path("", include("modules.users.urls")),
    path("auth/", include("api.globals.auth")),
    path("challenges/", include("modules.challenges.urls")),
    path("schema/", include("api.v1.schema"))
]

urlpatterns = [
    path("api/v1/", include(urls)),
]
