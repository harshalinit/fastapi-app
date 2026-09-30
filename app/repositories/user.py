from sqlalchemy import UUID

from app.models.user import User

class UserRepository:

    def get_user(self, user_id : UUID) -> User | None:
        pass

    def create_user(self, user : User) -> User | None:
        pass
    
    def update_user(self, user : User) -> User | None:
        pass 

    def delete_user(self, user_id : UUID) -> User | None:
        pass