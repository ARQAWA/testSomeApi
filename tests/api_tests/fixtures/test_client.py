from http import HTTPStatus
from typing import (
    Any,
    Literal,
    TypeVar,
    cast,
)
from unittest.mock import patch

import pytest
from httpx import (
    Client,
    Response,
)
from pydantic import BaseModel

BaseModelSchema = TypeVar("BaseModelSchema", bound=BaseModel)


class TestResponse(Response):
    @property
    def string_path(self) -> str:
        return f"{self.request.method} {self.request.url}"

    def check_status(self, expected_status: HTTPStatus) -> None:
        assert self.status_code == expected_status, repr(
            (
                f"Неожиданный статус ответа от {self.string_path}",
                self.request,
                self.text,
            )
        )


@pytest.fixture(scope="session")
def _test_client(api_conf):
    test_client = Client(base_url=api_conf.base_url, timeout=api_conf.timeout)
    yield test_client
    test_client.close()


@pytest.fixture
def api_call(_test_client):
    def _req(
        method: Literal["GET", "POST"],
        url: str,
        *,
        path_kw: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
        body: dict[str, Any] | None = None,
    ) -> TestResponse:
        if path_kw:
            url = url.format(**path_kw)

        with patch("httpx._transports.default.Response", TestResponse):
            res = _test_client.request(
                method,
                url,
                params=params,
                headers=headers,
                json=body,
            )

        assert type(res) is TestResponse
        return cast(TestResponse, res)

    return _req
