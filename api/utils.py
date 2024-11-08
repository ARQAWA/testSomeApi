from http import HTTPStatus

from httpx import Response


def check_response_status(response: Response, expected_status: HTTPStatus) -> None:
    assert response.status_code == expected_status, repr(("Неожиданный ответ", response.status_code, response.text))
