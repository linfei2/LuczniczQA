import pytest
import requests

import config


@pytest.fixture
def post_university(headers, university_data):
    university = requests.post(
        config.BASE_URL + "/university",
        headers=headers,
        json=university_data,
    )
    university_id = university.json()["data"][0]["id"]
    university_data = university.json()["data"][0]
    yield university_id, university_data


@pytest.fixture
def delete_university(headers, post_university):
    university_id = post_university[0]
    delete_response = requests.delete(
        config.BASE_URL + f"/university/{university_id}",
        headers=headers,
    )
    yield university_id, delete_response


@pytest.fixture
def update_university(headers, post_university):
    university_id = post_university[0]
    body = post_university[1]
    body["name"] = "Updated name"
    update_response = requests.put(
        config.BASE_URL + f"/university/{university_id}", headers=headers, json=body
    )
    yield university_id, update_response
    requests.delete(config.BASE_URL + f"/university/{university_id}", headers=headers)
