import pytest
import requests
from assertpy import assert_that

import config


@pytest.fixture
def generate_token():
    headers = config.BASE_HEADERS
    body = {"username": config.USER_NAME, "password": config.PASSWORD}

    response = requests.post(
        config.BASE_URL + "/admin/login", headers=headers, json=body
    )
    assert_that(response.status_code).is_equal_to(200)
    return response.json()["data"][0]["access_token"]


@pytest.fixture
def headers(generate_token):
    return {"accept": "application / json", "Authorization": f"Bearer {generate_token}"}
