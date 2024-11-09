from http import HTTPStatus
from uuid import uuid4

import pytest

from api.schemas.random_string.schemas import (
    CreateRandomStringResponseSchema,
    RandomStringResponseSchema,
)


@pytest.fixture
def get_random_string_data(api_call, urls):
    def inner(palindrome: bool):
        res = api_call("POST", urls.random_string_create, body={"palindrome": palindrome})
        return CreateRandomStringResponseSchema.from_response(res)

    return inner


@pytest.mark.parametrize(
    "request_id",
    (
        "123",
        1234,
        123.4,
        True,
        None,
    ),
)
def test_get_random_string_should_fail_validation(api_call, urls, request_id):
    res = api_call("GET", urls.random_string_get, path_kw={"request_id": request_id})
    res.check_status(HTTPStatus.UNPROCESSABLE_ENTITY)


def test_get_random_string_should_fail_not_found(api_call, urls):
    res = api_call("GET", urls.random_string_get, path_kw={"request_id": uuid4()})
    res.check_status(HTTPStatus.NOT_FOUND)


@pytest.mark.parametrize("palindrome_flag", (True, False))
def test_get_random_string_should_pass(api_call, urls, get_random_string_data, palindrome_flag):
    random_string_data = get_random_string_data(palindrome_flag)
    res = api_call("GET", urls.random_string_get, path_kw={"request_id": random_string_data.id})
    res.check_status(HTTPStatus.OK)
    res_data = RandomStringResponseSchema.from_response(res)
    assert res_data.result == random_string_data.result, "Данные не совпадают"
    if palindrome_flag:
        assert res_data.result == res_data.result[::-1], "Строка не является палиндромом"
