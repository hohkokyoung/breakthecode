from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from api.globals.permissions import IsInGroup
from modules.core.enums import GroupName
from .serializers import ChallengeAnswerSerializer, ChallengeHintSerializer

challenge_answer = "481139"

# Create your views here.
class ChallengeGuessView(APIView):
    throttle_scope = 'challenges'

    def post(self, request, *args, **kwargs):
        serializer = ChallengeAnswerSerializer(data=request.data)
        if serializer.is_valid():
            # If the data is valid, you can process it
            validated_data = serializer.validated_data
            if (validated_data != challenge_answer):
                return Response({"success": False, "message": "Please try again."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ChallengeHintListView(APIView):
    def get(self, request):

        hints = [
            {"sequence_no": 1, "hint": "This is the first hint."},
            {"sequence_no": 2, "hint": "This is the second hint."},
            {"sequence_no": 3, "hint": "This is the third hint."}
        ]

        serializer = ChallengeHintSerializer(hints, many=True)
        return Response(serializer.data)
    
class ChallengeCodeDetailView(APIView):
    permission_classes = [IsAuthenticated, IsInGroup(GroupName.PREMIUM.value)]

    def get(self, request, code_id, *args, **kwargs):
        if (code_id == 2):
            return Response({"code": challenge_answer[code_id - 1]})
        
        return Response({"detail": "Not found."})
