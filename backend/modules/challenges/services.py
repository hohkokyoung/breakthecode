from modules.challenges import challenge_answer

class ChallengeService:
    def get_challenge_code(self, code_id):
        # Assuming 'challenge_answer' is a predefined list of codes
        if code_id == 2:
            return {"code": challenge_answer[code_id - 1]}
        # Return None if the code is not found
        return None