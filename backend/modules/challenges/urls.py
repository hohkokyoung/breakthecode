from django.urls import path
from.views import ChallengeGuessView, ChallengeHintListView, ChallengeCodeDetailView

urlpatterns = [
    path('guess/', ChallengeGuessView.as_view(), name='challenge-guess'),
    path('hints/', ChallengeHintListView.as_view(), name='challenge-hints'),
    path('code/<int:code_id>/', ChallengeCodeDetailView.as_view(), name='challenge-code'),
]