import pytest
import requests

from assertpy import assert_that


@pytest.fixture
def post_and_delete_university(generate_token):
    university = requests.post("http://127.0.0.1:8080/university",
                       headers={
                           "accept": "application / json",
                           "Authorization": f"Bearer {generate_token}"
                       },
                       json={
                           "name": "Poznan University of Technology",
                           "city": "Poznan",
                           "timezone": "Europe/Warsaw"
                       })
    university_id = university.json()["data"][0]["id"]
    university_data = university.json()
    yield university_id, university_data
    delete_university = requests.delete(f"http://127.0.0.1:8080/university/{university_id}")
    assert_that(delete_university).is_equal_to(200)
