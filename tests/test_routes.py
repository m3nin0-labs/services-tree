#
# Copyright (C) 2024 Services Tree.
#
# Services Tree is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

import uuid

import pytest

from services_tree import service
from services_tree.db import Service


#
# Fixtures
#
@pytest.fixture
def service_items(service_document):
    """Create service items."""

    services = []
    for i in range(5):
        service_obj = Service(**service_document)

        service.create(service_obj)

    return services


def test_create_service(client, service_document):
    """Test service creation operation."""
    response = client.post("/services", json=service_document)
    response_document = response.json()

    # checking response
    assert response.status_code == 200  # noqa

    # checking id
    assert "id" in response_document

    # checking base metadata
    assert response_document["name"] == service_document["name"]

    # checking create/update dates
    assert "created" in response_document
    assert "updated" in response_document


def test_read_service(client, service_document):
    """Test service read operation."""
    response = client.post("/services", json=service_document)
    response_document = response.json()

    service_id = response_document["id"]

    # reading
    response = client.get(f"/services/{service_id}")
    current_service = response.json()

    assert response.status_code == 200  # noqa
    assert current_service["name"] == service_document["name"]

    # reading invalid service
    service_id = str(uuid.uuid4())
    response = client.get("f/services/{service_id}")

    assert response.status_code == 404  # noqa


def test_search_services(client, service_items):
    """Test services search operation."""
    response = client.get("/services")
    response_document = response.json()

    assert response.status_code == 200  # noqa

    assert len(response_document) > 0
    assert isinstance(response_document, list)

    # search query text
    response = client.get("/services", params={"q": "service"})

    assert response.status_code == 200 #noqa


def test_update_service(client, service_document):
    """Test service update operation."""
    response = client.post("/services", json=service_document)
    current_document = response.json()

    # preparing new document
    next_document = current_document.copy()
    next_document.update({"name": "UPDATED SERVICE!"})

    response = client.put(f"/services/{current_document['id']}", json=next_document)
    next_document_response = response.json()

    assert response.status_code == 200 #noqa
    assert next_document_response["name"] == next_document["name"]
