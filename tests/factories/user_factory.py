from app.config.security import get_password_hash
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