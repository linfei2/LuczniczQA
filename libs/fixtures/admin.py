import pytest
import requests
from assertpy import assert_that


@pytest.fixture
def generate_token():
    gt = requests.post(
        "http://127.0.0.1:8080/admin/login",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json={
            "username": "dmatczynska@example.com",
            "password": "super_secret_password",
        },
    )
    assert_that(gt.status_code).is_equal_to(200)
    return gt.json()["data"][0]["access_token"]
