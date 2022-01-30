from re import A
from urllib import request
from fastapi.testclient import TestClient

from tests.factories.user_factory import UserFactory
from app.models.user import User
import pytest

# @pytest.mark.asyncio
# def test_list_all_users(client: TestClient) -> None:
#     atributos = UserFactory.get_valid_user_properties()
#     user = User(**atributos)
#     user.save()
    
#     response = client.get("/users/")
#     content = response.json()

#     assert response.status_code == 200
#     assert len(content) == 1

def test_create_user(client: TestClient) -> None:   
    request_body = UserFactory.get_valid_user_request()

    response = client.post("/users/", json=request_body)
    content = response.json()

    assert response.status_code == 200
    assert content["name"] == request_body["name"]

@pytest.mark.parametrize('attribute', [
    ('name'),
    ('email'),
    ('password')
])
def test_create_user_missing_attribute(client: TestClient, attribute: str) -> None:   
    request_body = UserFactory.get_valid_user_request()

    del request_body[attribute]

    response = client.post("/users/", json=request_body)
    content = response.json()

    assert response.status_code == 400
