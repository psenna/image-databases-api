from app.model.user import User

class UserFactory():
    @classmethod
    def get_valid_user_properties(cls):
        return {
        "id": 0,
        "name": "Nome pessoa",
        "email": "pessoa@email.com",
        "hash_password": "aaaaaaaa",
    }