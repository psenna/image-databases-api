from typing import Dict
from app.config.security import get_password_hash, create_access_token
from app.models.user import User

class UserFactory():
    @classmethod
    def get_valid_user_properties(cls, props:Dict = {}):
        default_props = {
            "id": 0,
            "name": "Nome pessoa",
            "email": "pessoa@email.com",
            "hash_password": get_password_hash("password"),
        }

        return default_props | props


    @classmethod
    def get_valid_user_request(cls, props:Dict = {}):
        default_props = {
            "id": 0,
            "name": "Nome pessoa",
            "email": "pessoa@email.com",
            "password": "password",
        }

        return default_props | props

    
    @classmethod
    async def create(cls, props:Dict = {}) -> User:
        new_user = User(**cls.get_valid_user_properties(props=props))
        await new_user.save()
        return new_user

    @classmethod
    async def get_super_user_token_headers(cls):
        props = {'is_superuser': True, 'email': 'superuser@mail.com'}
        user = User(**cls.get_valid_user_properties(props=props))
        await user.save()
        token = create_access_token(user.id)
        return {"Authorization": f"Bearer {token}"}

    @classmethod
    async def get_regular_user_token_headers(cls):
        props = {'is_superuser': False, 'email': 'regularuser@mail.com'}
        user = User(**cls.get_valid_user_properties(props=props))
        await user.save()
        token = create_access_token(user.id)
        return {"Authorization": f"Bearer {token}"}
