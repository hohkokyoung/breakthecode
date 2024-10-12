from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from api.globals.permissions import IsInGroup
from modules.core.enums import GroupName
from .serializers import ChallengeAnswerSerializer, ChallengeHintSerializer
from .services import ChallengeService
from modules.challenges import challenge_answer
from injector import inject

# Create your views here.
class ChallengeGuessView(APIView):
    throttle_scope = 'challenges'

    def post(self, request, *args, **kwargs):
        serializer = ChallengeAnswerSerializer(data=request.data)
        if serializer.is_valid():
            # If the data is valid, you can process it
            validated_data = serializer.validated_data
            if (validated_data["code"] != challenge_answer):
                return Response({"success": False, "message": "Please try again."}, status=status.HTTP_200_OK)
            else:
                return Response({"success": True, "message": "Well Done!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ChallengeHintListView(APIView):
    def get(self, request):

        hints = [
            {"sequence_no": 1, "hint": "A user has this information."},
            {"sequence_no": 2, "hint": "Maybe we can reuse the same user for further exploit."},
            {"sequence_no": 3, "hint": "What could be behind the image?"},
            {"sequence_no": 4, "hint": "Hidden behind third code."},
            {"sequence_no": 5, "hint": "First two digits of the developer's CGPA."},
        ]

        serializer = ChallengeHintSerializer(hints, many=True)
        return Response(serializer.data)
    
class ChallengeCodeDetailView(APIView):
    permission_classes = [IsAuthenticated, IsInGroup(GroupName.PREMIUM.value)]

    @inject
    def __init__(self, challenge_service: ChallengeService, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.challenge_service = challenge_service

    def get(self, request, code_id, *args, **kwargs):
        code = self.challenge_service.get_challenge_code(code_id)
        return Response(code)