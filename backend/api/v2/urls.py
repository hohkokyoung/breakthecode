from django.contrib import admin
from django.urls import path, include
from modules.challenges import urls as challenge_urls

# Filter out the 'challenge-code' URL
challenge_urlpatterns = [url for url in challenge_urls.urlpatterns if url.name != 'challenge-code']

urlpatterns = [
    path("", include("modules.users.urls")),
    path("auth/", include("api.globals.auth")),
    # reverse('<namespace>:<app_name>:<url_name>')
    path("challenges/", include((challenge_urlpatterns, 'challenges'), namespace='challenges')),
    path("schema/", include("api.v2.schema"))
]
