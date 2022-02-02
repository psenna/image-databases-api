import json
from typing import Dict
from fastapi.testclient import TestClient
import ormar
import pytest
from app.models.image import Image
from app.models.label import Label
from tests.factories.dataset_factory import DatasetFactory
from tests.factories.image_factory import ImageFactory
from tests.factories.label_factory import LabelFactory

@pytest.mark.asyncio
async def test_create_label_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    request_body = LabelFactory.get_valid_request()

    response = client.post(
        "/labels/",
         json=request_body,
         headers=regular_user_token_header)

    content = response.json()

    assert response.status_code == 200
    assert content["name"] == request_body["name"]
    dataset_label = await Label.objects.get(id=content["id"])
    assert dataset_label.name == request_body["name"]

@pytest.mark.asyncio
async def test_cant_create_label_unlogged_user(client: TestClient) -> None:   
    request_body = LabelFactory.get_valid_request()

    response = client.post(
        "/labels/",
         json=request_body)

    assert response.status_code == 401

@pytest.mark.asyncio
async def test_list_all_labels_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    label = await LabelFactory.create()
    
    response = client.get(
        "/labels/",
        headers=regular_user_token_header)

    content = response.json()

    assert response.status_code == 200
    assert content['total'] == 1

@pytest.mark.asyncio
async def test_cant_list_all_labels_with_unlogged_user(client: TestClient) -> None:   
    label = await LabelFactory.create()
    
    response = client.get(
        "/labels/")

    content = response.json()

    assert response.status_code == 401

@pytest.mark.asyncio
async def test_list_one_label_with_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    label = await LabelFactory.create()
    
    response = client.get(
        f"/labels/{label.id}",
        headers=regular_user_token_header)

    content = response.json()

    assert response.status_code == 200
    assert content["name"] == label.name

@pytest.mark.asyncio
async def test_cant_list_one_label_with_unlogged_user(client: TestClient) -> None:   
    label = await LabelFactory.create()
    
    response = client.get(
        f"/labels/{label.id}")

    content = response.json()

    assert response.status_code == 401

@pytest.mark.asyncio
async def test_update_one_label_with_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    label = await LabelFactory.create()

    update_request = {"name": "new_label_name"}
    
    response = client.patch(
        f"/labels/{label.id}",
        json=update_request,
        headers=regular_user_token_header)

    content = response.json()

    assert response.status_code == 200
    assert content["name"] != label.name
    database_label = await Label.objects.get(id=label.id)
    assert database_label.name == update_request["name"]


@pytest.mark.asyncio
async def test_cant_update_one_label_with_unlogged_user(client: TestClient) -> None:   
    label = await LabelFactory.create()

    update_request = {"name": "new_label_name"}
    
    response = client.patch(
        f"/labels/{label.id}",
        json=update_request)

    content = response.json()

    assert response.status_code == 401
    database_label = await Label.objects.get(id=label.id)
    assert database_label.name == label.name
    assert database_label.name != update_request["name"]

@pytest.mark.asyncio
async def test_delete_one_label_with_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    label = await LabelFactory.create()

    response = client.delete(
        f"/labels/{label.id}",
        headers=regular_user_token_header)

    content = response.json()

    assert response.status_code == 200
    with pytest.raises(ormar.exceptions.NoMatch): 
        database_label = await Label.objects.get(id=label.id)

@pytest.mark.asyncio
async def test_cant_delete_one_label_with_unlogged_user(client: TestClient) -> None:   
    label = await LabelFactory.create()
    
    response = client.delete(
        f"/labels/{label.id}")

    content = response.json()

    assert response.status_code == 401
    database_label = await Label.objects.get(id=label.id)
    assert database_label.id == label.id

@pytest.mark.asyncio
async def test_delete_one_label_in_some_images_with_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    dataset = await DatasetFactory.create()
    image = await ImageFactory.create(dataset.id)
    image2 = await ImageFactory.create(dataset.id)
    label = await LabelFactory.create()
    await image.labels.add(label)
    await image2.labels.add(label)

    response = client.delete(
        f"/labels/{label.id}",
        headers=regular_user_token_header)

    content = response.json()

    assert response.status_code == 200
    with pytest.raises(ormar.exceptions.NoMatch): 
        database_label = await Label.objects.get(id=label.id)
    await Image.objects.get(id=image.id)
    await Image.objects.get(id=image2.id)

    