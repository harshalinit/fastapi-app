from sqlalchemy import UUID

from app.models.user import User

class AuthRepository:

    def get(self, user_id : UUID) -> User | None:
        pass

    def create(self, user : User) -> User | None:
        pass
    
    def update(self, user : User) -> User | None:
        pass 

    def delete(self, user_id : UUID) -> User | None:
        pass