from random import choices
from uuid import (
    UUID,
    uuid4,
)

from fastapi import (
    FastAPI,
    HTTPException,
)
from pydantic import BaseModel

app = FastAPI()

storage = {}


class PalindromeRequest(BaseModel):
    palindrome: bool


class ResultResponse(BaseModel):
    result: str


class CreateResultResponse(ResultResponse):
    id: UUID


def generate_palindrome():
    half = "".join(choices("abcdefghijklmnopqrstuvwxyz", k=3))
    return half + half[::-1]


def generate_random_string():
    return "".join(choices("abcdefghijklmnopqrstuvwxyz", k=6))


@app.post("/api/v1/random_string")
async def generate_string(request: PalindromeRequest) -> CreateResultResponse:
    new_id = uuid4()
    result = generate_palindrome() if request.palindrome else generate_random_string()
    storage[new_id] = result
    return CreateResultResponse(id=new_id, result=result)


@app.get("/api/v1/random_string/{request_id}", response_model=ResultResponse)
async def get_result(request_id: UUID) -> ResultResponse:
    if request_id in storage:
        return ResultResponse(result=storage[request_id])
    else:
        raise HTTPException(status_code=404, detail="Result not found")
