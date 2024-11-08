import pytest

from api.settings import ApiSettings


@pytest.fixture(scope="session")
def api_conf():
    return ApiSettings()
