from uuid import UUID

from api.base_model import BaseResponseModel


class RandomStringResponseSchema(BaseResponseModel):
    result: str


class CreateRandomStringResponseSchema(RandomStringResponseSchema):
    id: UUID
