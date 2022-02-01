import json
from typing import Dict
from fastapi.testclient import TestClient
import ormar
import pytest

from app.models.image import Image
from tests.factories.dataset_factory import DatasetFactory
from tests.factories.image_factory import ImageFactory

@pytest.mark.asyncio
async def test_create_image_with_regularuser(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:    
    dataset = await DatasetFactory.create_dataset()
    
    image_request = ImageFactory.get_valid_dataset_request(dataset.id)
    
    response = client.post("/images/", json=image_request, headers=regular_user_token_header)
    content = response.json()
    
    assert response.status_code == 200
    assert content['thumbnail'] == 'iVBORw0KGgoAAAANSUhEUgAAACQAAAAYCAYAAACSuF9OAAAEf0lEQVR4nNWWzWsTWxjGf+dMZtLWr0bQWuIHIipFN4IupIIgKC4VLSiK+Ae4dKciIohQBN3pWkVEQdyKdVFEiRXBRUVtmkwaKImlFpHGzJyvu5DMzdje5q6u3mc3c55z3ud9n/c9M8I55/iDIH+3gF+xpKCbN2/y+fNnjDFYa5mdncVaS7PZTDhKKS5dusSTJ094/fo18/PzKKWw1iYc5xwvXrygXq8TxzHGGH78+IFzjl8NyiwlqNFo8PTpU4QQSClZu3YtFy9e5P3793R1df3MSEpWrlzJxMQExWKR0dFRuru7uX37Nh8+fABACMGXL1949+5dcvauXbs4e/YsYRjied6/EwRQqVSSLLq7u7HW4vt+si6EIAxDnHMIIQBYv3596gylFJ7nJTyAgYEBcrlcSgx0sOzw4cMUi0WmpqaoVqtorcnn8wRBsEBQsVikXq/T39+Pc47t27f/HURKms0mk5OTVKtVZmZmmJub49ChQylrAcRSU2atRUrJ+fPn6erq4sKFCxQKBfbu3Ysxhp6enoR369YtfN/n9OnTPH/+nCNHjlCr1cjn88l5Dx8+ZGxsjD179jAwMMDq1atZt24dUsqkUktaJqVk9+7dxHGMlJJyucyxY8eYn59n1apVCe/+/fvcuHGDNWvWUKlUGBoaQilFX18f1lo8z8MYw9WrV+nv7+fx48cMDQ1x4sQJcrlc0o8dKwSgtcYYgxACz/MWeN5ezSiKmJ6eZsuWLYtyWr3USrDd+hY6NnUmkyGTyeCcW+B3O6SUqUwXg+/7yVBIuXj7JoK01mityWazCCGw1iZT04IQInVvtHqshTiOF9wtxpgFVY3jGCBJoGUrtFnWaDTIZrMYY5BSLnpptQtyzhGGIZs3b05VqRWg/V37c8v+9kQajQa9vb3pCrUmxvM8tNapzl8Mzrl/7INfq9GJ076eyGw0GkRRlARSSv1jAGvtohVsobWutV5geycklsVxzIMHD3DOEQQB9XqdsbExtm7dypUrV5INly9fZtOmTcDPJp2enqZUKnHnzp2E8+bNGz59+kSz2aRarXLw4EH27duH1jp1yy+GpEKZTIZSqUSpVOLjx498/fqVt2/fpgIB9PX1UalUCMOQyclJhBA8evQoxdm2bRthGFKr1fB9n4mJCQYHB5mbm+tYodTYl0ql5JtkjCGfz7Njx47UhuXLl1MoFBLezp07OXDgQIqzYsUKyuUy8LPXNm7cSLPZJJvN/ntB1lpOnjyJUoogCCiXy9y9exetdWpDEAQcP36cWq3G9+/f0Vrz8uXLFEcIwf79++nt7cUYw9TUFEEQsGzZso6CUpYNDg6itebZs2dcu3aNmZkZNmzYwKtXr5INR48eJZfL4fs+IyMjDA8P09PTw5kzZ1LiT506xezsLEopRkdHCYKAb9++MTIysrQi14Y4jt29e/fc+Pi4U0o5Y4xTSrVTXBRF7ty5c65QKLgoipwxxllrXRzHCUcp5YaHh93169fd+Pi4i6IoeW+tdUuh47fsv8b/65/6d+CPE/QXF+GuvsnzNBYAAAAASUVORK5CYII='

@pytest.mark.asyncio
async def test_list_all_images_with_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:
    dataset = await DatasetFactory.create_dataset()
    
    image_properties = ImageFactory.get_valid_dataset_properties(dataset.id)

    image = Image(**image_properties)
    await image.save()

    response = client.get("/images/", headers=regular_user_token_header)
    content = response.json()

    assert response.status_code == 200
    assert len(content) == 1

@pytest.mark.asyncio
async def test_get_one_image_with_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:
    dataset = await DatasetFactory.create_dataset()
    
    image_properties = ImageFactory.get_valid_dataset_properties(dataset.id)

    image = Image(**image_properties)
    await image.save()

    response = client.get(f"/images/{image.id}", headers=regular_user_token_header)
    content = response.json()

    assert response.status_code == 200
    assert content['thumbnail'].encode('UTF-8') == image.thumbnail
    assert content['data'].encode('UTF-8') == image.data

@pytest.mark.asyncio
async def test_cant_get_one_image_with_unlogged_user(client: TestClient) -> None:
    dataset = await DatasetFactory.create_dataset()
    
    image_properties = ImageFactory.get_valid_dataset_properties(dataset.id)

    image = Image(**image_properties)
    await image.save()

    response = client.get(f"/images/{image.id}")
    content = response.json()

    assert response.status_code == 401

@pytest.mark.asyncio
async def test_delete_one_image_with_regular_user(client: TestClient, regular_user_token_header: Dict[str, str]) -> None:
    dataset = await DatasetFactory.create_dataset()
    
    image_properties = ImageFactory.get_valid_dataset_properties(dataset.id)

    image = Image(**image_properties)
    await image.save()

    response = client.delete(f"/images/{image.id}", headers=regular_user_token_header)
    content = response.json()

    assert response.status_code == 200
    with pytest.raises(ormar.exceptions.NoMatch): 
        await Image.objects.get(id=image.id)


@pytest.mark.asyncio
async def test_cant_delete_one_image_with_unlogged_user(client: TestClient) -> None:
    dataset = await DatasetFactory.create_dataset()
    
    image_properties = ImageFactory.get_valid_dataset_properties(dataset.id)

    image = Image(**image_properties)
    await image.save()

    response = client.delete(f"/images/{image.id}")
    content = response.json()

    assert response.status_code == 401
    await Image.objects.get(id=image.id)    