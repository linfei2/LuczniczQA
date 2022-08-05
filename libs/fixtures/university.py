import pytest
import requests


@pytest.fixture
def post_university(generate_token, university_data):
    university = requests.post(
        "http://127.0.0.1:8080/university",
        headers={
            "accept": "application / json",
            "Authorization": f"Bearer {generate_token}",
        },
        json=university_data,
    )
    university_id = university.json()["data"][0]["id"]
    university_data = university.json()["data"][0]
    yield university_id, university_data


@pytest.fixture
def delete_university(headers, post_university):
    university_id = post_university[0]
    delete_response = requests.delete(
        f"http://127.0.0.1:8080/university/{university_id}",
        headers=headers,
    )
    yield university_id, delete_response


@pytest.fixture
def update_university(headers, post_university):
    university_id = post_university[0]
    body = post_university[1]
    body["name"] = "Updated name"
    update_response = requests.put(
        f"http://127.0.0.1:8080/university/{university_id}", headers=headers, json=body
    )
    yield university_id, update_response
    requests.delete(
        f"http://127.0.0.1:8080/university/{university_id}", headers=headers
    )
