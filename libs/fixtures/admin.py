import pytest
import requests
from assertpy import assert_that


@pytest.fixture
def generate_token():
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    body = {"username": "dmatczynska@example.com", "password": "super_secret_password"}

    response = requests.post(
        "http://127.0.0.1:8080/admin/login", headers=headers, json=body
    )
    assert_that(response.status_code).is_equal_to(200)
    return response.json()["data"][0]["access_token"]


@pytest.fixture
def headers(generate_token):
    return {"accept": "application / json", "Authorization": f"Bearer {generate_token}"}
