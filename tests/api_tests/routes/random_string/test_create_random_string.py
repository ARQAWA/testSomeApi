from http import HTTPStatus

import pytest

from api.schemas.random_string.schemas import CreateRandomStringResponseSchema
from api.utils import check_response_status


@pytest.mark.parametrize(
    "payload",
    (
        {"palindrome": "asdsada"},
        {"palindrome": 1245},
        {"palindrome": None},
        {"other_field": "other_value"},
        "any_text",
        True,
        None,
    ),
)
def test_create_random_string_should_fail(
    random_string_create_url,
    make_request,
    payload,
):
    res = make_request("POST", random_string_create_url, body=payload)
    check_response_status(res, HTTPStatus.UNPROCESSABLE_ENTITY)


@pytest.mark.parametrize("palindrome_flag", (True, False))
def test_create_random_string_should_pass(
    random_string_create_url,
    make_request,
    palindrome_flag,
):
    payload = {"palindrome": palindrome_flag}
    res = make_request("POST", random_string_create_url, body=payload)
    check_response_status(res, HTTPStatus.OK)
    res_data = CreateRandomStringResponseSchema.from_response(res)
    if palindrome_flag:
        assert res_data.result == res_data.result[::-1], "Строка не палиндром"
