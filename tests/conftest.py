#
# Copyright (C) 2024 Services Tree.
#
# Services Tree is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

import pytest
from fastapi.testclient import TestClient

from services_tree.main import app as base_app


@pytest.fixture
def app():
    """Application fixture."""
    return base_app


@pytest.fixture
def client(app):
    """Test client."""
    return TestClient(app)


@pytest.fixture
def service_document():
    """Simple service document fixture."""
    return {
        "name": "Simple Service",
        "description": "A very simple service",
        "url": "http://random-address.com",
    }
