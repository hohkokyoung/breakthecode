from rest_framework import serializers

class ChallengeAnswerSerializer(serializers.Serializer):
    code = serializers.CharField(required=True, min_length=6, max_length=6)

class ChallengeHintSerializer(serializers.Serializer):
    sequence_no = serializers.IntegerField()
    hint = serializers.CharField(max_length=255)
