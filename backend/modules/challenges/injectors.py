
from injector import Module, provider
from .services import ChallengeService  

class ChallengeModule(Module):
    @provider
    def provide_challenge_service(self) -> ChallengeService:
        return ChallengeService()