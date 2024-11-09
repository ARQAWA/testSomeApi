import pytest
from pydantic import (
    BaseModel,
    ConfigDict,
)

from tests.api_tests.fixtures.test_client import TestResponse


class BaseResponseModel(BaseModel):
    @classmethod
    def from_response(cls, response: TestResponse) -> "BaseResponseModel":
        # noinspection PyBroadException
        try:
            return cls.model_validate_json(response.content)
        except Exception:
            pytest.fail(f"Ошибка валидации ответа от {response.string_path} моделью {cls.__name__}")

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )
