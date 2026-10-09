import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    """Provide a TestClient with a clean in-memory activity state."""
    original_activities = copy.deepcopy(activities)
    activities.clear()
    activities.update(copy.deepcopy(original_activities))

    with TestClient(app) as test_client:
        yield test_client

    activities.clear()
    activities.update(copy.deepcopy(original_activities))
