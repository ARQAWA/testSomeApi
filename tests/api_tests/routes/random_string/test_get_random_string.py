from http import HTTPStatus
from uuid import uuid4

import pytest

from api.schemas.random_string.schemas import (
    CreateRandomStringResponseSchema,
    RandomStringResponseSchema,
)
from api.utils import check_response_status


@pytest.fixture
def get_random_string_data(random_string_create_url, make_request):
    def inner(palindrome: bool):
        res = make_request("POST", random_string_create_url, body={"palindrome": palindrome})
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
def test_get_random_string_should_fail_validation(random_string_get_url, make_request, request_id):
    res = make_request(
        "GET",
        random_string_get_url,
        path_kw={"request_id": request_id},
    )
    check_response_status(res, HTTPStatus.UNPROCESSABLE_ENTITY)


def test_get_random_string_should_fail_not_found(random_string_get_url, make_request):
    res = make_request(
        "GET",
        random_string_get_url,
        path_kw={"request_id": uuid4()},
    )
    check_response_status(res, HTTPStatus.NOT_FOUND)


@pytest.mark.parametrize("palindrome_flag", (True, False))
def test_get_random_string_should_pass(random_string_get_url, get_random_string_data, make_request, palindrome_flag):
    random_string_data = get_random_string_data(palindrome_flag)
    res = make_request(
        "GET",
        random_string_get_url,
        path_kw={"request_id": random_string_data.id},
    )

    check_response_status(res, HTTPStatus.OK)
    res_data = RandomStringResponseSchema.from_response(res)
    assert res_data.result == random_string_data.result, "Данные не совпадают"
    if palindrome_flag:
        assert res_data.result == res_data.result[::-1], "Строка не является палиндромом"
