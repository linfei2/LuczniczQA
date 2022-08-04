import pytest
import requests
from assertpy import assert_that, soft_assertions


@pytest.mark.university
class TestUniversity:
    def test_01_get_list_of_universities(self, generate_token):
        uni_list = requests.get(
            "http://127.0.0.1:8080/university/",
            headers={
                "accept": "application / json",
                "Authorization": f"Bearer {generate_token}",
            },
        )

        with soft_assertions():
            assert_that(uni_list.status_code).is_equal_to(200)

    def test_02_get_university(self, generate_token, post_university):
        uni_id = post_university[0]
        response = requests.get(
            f"http://127.0.0.1:8080/university/{uni_id}",
            headers={
                "accept": "application / json",
                "Authorization": f"Bearer {generate_token}",
            },
        )

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.json()["message"]).is_equal_to(
                "University data retrieved successfully"
            )
            assert_that(post_university[1]).contains_key(
                "id", "name", "city", "timezone", "current_time"
            )

    def test_03_delete_university(self, generate_token, delete_university):
        get_deleted_uni = requests.get(
            f"http://127.0.0.1:8080/university/{delete_university[0]}",
            headers={
                "accept": "application / json",
                "Authorization": f"Bearer {generate_token}",
            },
        )
        with soft_assertions():
            assert_that(delete_university[1].status_code).is_equal_to(200)
            assert_that(get_deleted_uni.status_code).is_equal_to(404)
