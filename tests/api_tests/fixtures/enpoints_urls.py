import pytest


@pytest.fixture
def random_string_create_url():
    return "/api/v1/random_string"


@pytest.fixture
def random_string_get_url():
    return "/api/v1/random_string/{request_id}"
