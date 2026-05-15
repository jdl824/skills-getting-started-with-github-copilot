import copy

from fastapi.testclient import TestClient
from pytest import fixture

from src.app import app, activities


@fixture
def client():
    return TestClient(app)


@fixture(autouse=True)
def reset_activities():
    original_activities = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(copy.deepcopy(original_activities))
