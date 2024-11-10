from http import HTTPStatus

import pytest

from api.schemas.random_string.schemas import CreateRandomStringResponseSchema


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
def test_create_random_string_should_fail_validation(api_call, urls, payload):
    res = api_call("POST", urls.random_string_create, body=payload)
    res.check_status(HTTPStatus.UNPROCESSABLE_ENTITY)


@pytest.mark.parametrize("palindrome_flag", (True, False))
def test_create_random_string_should_pass(api_call, urls, palindrome_flag):
    payload = {"palindrome": palindrome_flag}
    res = api_call("POST", urls.random_string_create, body=payload)
    res.check_status(HTTPStatus.OK)
    res_data = CreateRandomStringResponseSchema.from_response(res)
    if palindrome_flag:
        assert res_data.result == res_data.result[::-1], "Строка не палиндром"
