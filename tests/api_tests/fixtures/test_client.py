from typing import (
    Any,
    Literal,
)

import pytest
from httpx import (
    Client,
    Response,
)


@pytest.fixture(scope="session")
def test_client(api_conf):
    yield Client(
        base_url=api_conf.base_url,
        timeout=api_conf.timeout,
    )


@pytest.fixture
def make_request(test_client):
    def _req(
        method: Literal["GET", "POST"],
        url: str,
        *,
        path_kw: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
        body: dict[str, Any] | None = None,
    ) -> Response:
        if path_kw:
            url = url.format(**path_kw)

        return test_client.request(
            method,
            url,
            params=params,
            headers=headers,
            json=body,
        )

    return _req
