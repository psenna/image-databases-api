from tests.factories.user_factory import UserFactory
from app.model.user import User
import pytest

def test_create_valid_user():
    attributes = UserFactory.get_valid_user_properties()
    user = User(**attributes)

def test_create_user_with_invalid_email():
    attributes = UserFactory.get_valid_user_properties()
    attributes['email'] = 'someInvalidString'
    with pytest.raises(ValueError, match='The user email format is invalid!'):
        user = User(**attributes)