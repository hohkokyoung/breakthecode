from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("modules.users.urls")),
    path("auth/", include("api.globals.auth")),
    path("challenges/", include("modules.challenges.urls")),
    path("schema/", include("api.v1.schema"))
]
