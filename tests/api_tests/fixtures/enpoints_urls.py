import pytest


class ApiUrls:
    random_string_create = "/api/v1/random_string"
    random_string_get = "/api/v1/random_string/{request_id}"


@pytest.fixture(scope="session")
def urls():
    return ApiUrls()
