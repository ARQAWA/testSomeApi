import pytest
from httpx import Response
from pydantic import (
    BaseModel,
    ConfigDict,
)


class BaseResponseModel(BaseModel):
    @classmethod
    def from_response(cls, response: Response) -> "BaseResponseModel":
        # noinspection PyBroadException
        try:
            return cls.model_validate_json(response.content)
        except Exception:
            pytest.fail(
                f"Failed to validate response by {cls.__name__} "
                f"for {response.request.method} {response.request.url}"
            )

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )
