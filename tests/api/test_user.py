from multiprocessing import context
import ormar
from fastapi.testclient import TestClient

from tests.factories.user_factory import UserFactory
from app.models.user import User
import pytest

@pytest.mark.asyncio
async def test_list_all_users(client: TestClient) -> None:
    atributos = UserFactory.get_valid_user_properties()
    user = User(**atributos)
    await user.save()
    
    response = client.get("/users/")
    content = response.json()

    assert response.status_code == 200
    assert len(content) == 1

async def test_create_user(client: TestClient) -> None:   
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
async def test_create_user_missing_attribute(client: TestClient, attribute: str) -> None:   
    request_body = UserFactory.get_valid_user_request()

    del request_body[attribute]

    response = client.post("/users/", json=request_body)
    content = response.json()

    assert response.status_code == 422

@pytest.mark.asyncio
async def test_get_user_by_id(client: TestClient) -> None:
    atributos = UserFactory.get_valid_user_properties()
    user = User(**atributos)
    await user.save()
    
    response = client.get(f"/users/{user.id}")
    content = response.json()

    assert response.status_code == 200
    assert content['id'] == user.id
    assert content['email'] == user.email
    assert content['name'] == user.name

async def test_get_non_existent_user_by_id(client: TestClient) -> None:  
    response = client.get(f"/users/1")
    content = response.json()

    assert response.status_code == 404

@pytest.mark.asyncio
@pytest.mark.parametrize('update_body', [
    {'name': 'new_name'},
    {'email': 'new_mail@mail.com'},
    {'name': 'new_name', 'email': 'new_mail@mail.com'}
])
async def test_update_user_by_id(client: TestClient, update_body) -> None:
    atributos = UserFactory.get_valid_user_properties()
    user = User(**atributos)
    await user.save()    
    
    response = client.patch(f"/users/{user.id}", json=update_body)
    content = response.json()

    assert response.status_code == 200
    assert content['id'] == user.id
    if 'email' in update_body.keys():
        assert content['email'] == update_body['email']

    if 'name' in update_body.keys():
        assert content['name'] == update_body['name']


async def test_update_non_existent_user_by_id(client: TestClient) -> None:  
    response = client.patch("/users/1", json={})

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_user_by_id(client: TestClient) -> None:
    atributos = UserFactory.get_valid_user_properties()
    user = User(**atributos)
    await user.save()    
    
    response = client.delete(f"/users/{user.id}")
    content = response.json()

    assert response.status_code == 200

    with pytest.raises(ormar.exceptions.NoMatch): 
        await User.objects.get(id=user.id)


async def test_delete_non_existent_user_by_id(client: TestClient) -> None:  
    response = client.delete("/users/1")

    assert response.status_code == 404

@pytest.mark.asyncio
@pytest.mark.parametrize('test_data', [
    {'body': {"email": "pessoa@email.com", "password": "password"}, 'status': 200},
    {'body': {"email": "notsameperson@email.com", "password": "password"}, 'status': 403},
    {'body': {"email": "pessoa@email.com", "password": "worng"}, 'status': 403},
    {'body': {"password": "worng"}, 'status': 422},
    {'body': {"email": "pessoa@email.com"}, 'status': 422},
])
async def test_login(client: TestClient, test_data) -> None:
    atributos = UserFactory.get_valid_user_properties()
    user = User(**atributos)
    await user.save()

    response = client.post(f"/users/login", json=test_data['body'])
    content = response.json()

    assert response.status_code == test_data['status']