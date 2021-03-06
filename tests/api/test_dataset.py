from typing import Dict
from fastapi.testclient import TestClient
import ormar
import pytest
from app.models.dataset import Dataset
from app.models.image import Image

from tests.factories.dataset_factory import DatasetFactory
from tests.factories.image_factory import ImageFactory


async def test_create_dataset_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    request_body = DatasetFactory.get_valid_dataset_request()

    response = client.post(
        "/datasets/",
         json=request_body,
         headers=regular_user_token_header)

    content = response.json()

    assert response.status_code == 200
    assert content["name"] == request_body["name"]

async def test_cant_create_dataset_unlogged_user(client: TestClient) -> None:   
    request_body = DatasetFactory.get_valid_dataset_request()

    response = client.post(
        "/datasets/",
         json=request_body)

    assert response.status_code == 401

@pytest.mark.asyncio
async def test_list_all_datasets_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    dataset = await DatasetFactory.create()

    response = client.get(
        "/datasets/",
        headers=regular_user_token_header)

    content = response.json()

    assert response.status_code == 200
    assert content['total'] == 1

@pytest.mark.asyncio
async def test_cant_list_all_datasets_unlogged_user(client: TestClient) -> None:   
    dataset = await DatasetFactory.create()

    response = client.get(
        "/datasets/")

    assert response.status_code == 401

@pytest.mark.asyncio
async def test_list_one_dataset_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    dataset = await DatasetFactory.create()
    
    response = client.get(
        f"/datasets/{dataset.id}",
        headers=regular_user_token_header)

    content = response.json()

    assert response.status_code == 200
    assert content["name"] == dataset.name

@pytest.mark.asyncio
async def test_list_one_inexistent_dataset_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    response = client.get(
        "/datasets/100",
        headers=regular_user_token_header)

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_cant_list_one_inexistent_dataset_with_unlogged_user(client: TestClient) -> None:   
    response = client.get("/datasets/100")

    assert response.status_code == 401

@pytest.mark.asyncio
async def test_cant_list_one_dataset_with_unlogged_user(client: TestClient) -> None:   
    dataset = await DatasetFactory.create()
    
    response = client.get(
        f"/datasets/{dataset.id}")

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_cant_update_dataset_with_unlogged_user(client: TestClient) -> None:   
    dataset = await DatasetFactory.create()

    update_request = {"name": "newDatasetName"}
    
    response = client.patch(
        f"/datasets/{dataset.id}",
        json=update_request)

    assert response.status_code == 401

@pytest.mark.asyncio
async def test_delete_empty_dataset_with_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    dataset = await DatasetFactory.create()
    
    response = client.delete(
        f"/datasets/{dataset.id}",
        headers=regular_user_token_header)

    assert response.status_code == 200
    with pytest.raises(ormar.exceptions.NoMatch): 
        await Dataset.objects.get(id=dataset.id)

@pytest.mark.asyncio
async def test_cant_delete_dataset_with_unlogged_user(client: TestClient) -> None:   
    dataset = await DatasetFactory.create()
    
    response = client.delete(
        f"/datasets/{dataset.id}")

    assert response.status_code == 401
    
    dataset_database = await Dataset.objects.get(id=dataset.id)
    assert dataset_database.id == dataset.id


@pytest.mark.asyncio
async def test_cant_delete_dataset_with_images_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    dataset = await DatasetFactory.create()
    image1 = await ImageFactory.create(dataset.id)
    image2 = await ImageFactory.create(dataset.id)
    
    response = client.delete(
        f"/datasets/{dataset.id}",
        headers=regular_user_token_header)

    assert response.status_code == 400
    await Dataset.objects.get(id=dataset.id)
    await Image.objects.get(id=image1.id)
    await Image.objects.get(id=image2.id)

@pytest.mark.asyncio
async def test_delete_all_images_in_dataset_with_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:   
    dataset = await DatasetFactory.create()
    image1 = await ImageFactory.create(dataset.id)
    image2 = await ImageFactory.create(dataset.id)
    
    response = client.delete(
        f"/datasets/{dataset.id}/images",
        headers=regular_user_token_header)

    assert response.status_code == 200
    dataset_saved = await Dataset.objects.select_related('images').get(id=dataset.id)
    assert len(dataset_saved.images) == 0
    with pytest.raises(ormar.exceptions.NoMatch): 
        await Image.objects.get(id=image1.id)
    with pytest.raises(ormar.exceptions.NoMatch): 
        await Image.objects.get(id=image2.id)
        