from app.config.security import get_password_hash, create_access_token
from app.models.user import User

class UserFactory():
    @classmethod
    def get_valid_user_properties(cls):
        return {
            "id": 0,
            "name": "Nome pessoa",
            "email": "pessoa@email.com",
            "hash_password": get_password_hash("password"),
        }

    @classmethod
    def get_valid_user_request(cls):
        return {
            "id": 0,
            "name": "Nome pessoa",
            "email": "pessoa@email.com",
            "password": "password",
        }
    
    @classmethod
    async def create(cls) -> User:
        new_user = User(**cls.get_valid_user_properties())
        await new_user.save()
        return new_user

    @classmethod
    async def get_super_user_token_headers(cls):
        user = User(**cls.get_valid_user_properties())
        user.email = 'superuser@mail.com'
        user.is_superuser = True
        await user.save()
        token = create_access_token(user.id)
        return {"Authorization": f"Bearer {token}"}

    @classmethod
    async def get_regular_user_token_headers(cls):
        user = User(**cls.get_valid_user_properties())
        user.email = 'regularuser@mail.com'
        await user.save()
        token = create_access_token(user.id)
        return {"Authorization": f"Bearer {token}"}
