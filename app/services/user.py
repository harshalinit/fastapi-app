from app.repositories.user import UserRepository
from app.models.user import User 

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_id : int) -> User | None:
        pass