from modules.challenges import challenge_answer

class ChallengeService:
    def get_challenge_code(self, code_id):
        if (code_id == 2):
            return {"code": challenge_answer[code_id - 1]}
        return {"detail": "Not found."}