import pytest
import requests
from assertpy import assert_that, soft_assertions

import config


@pytest.mark.university
class TestUniversity:
    def test_01_get_list_of_universities(self, headers):
        uni_list = requests.get(
            config.BASE_URL + "/university/",
            headers=headers,
        )

        with soft_assertions():
            assert_that(uni_list.status_code).is_equal_to(200)

    def test_02_get_university(self, headers, post_university):
        uni_id = post_university[0]
        response = requests.get(
            config.BASE_URL + f"/university/{uni_id}", headers=headers
        )

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.json()["message"]).is_equal_to(
                "University data retrieved successfully"
            )
            assert_that(post_university[1]).contains_key(
                "id", "name", "city", "timezone", "current_time"
            )

    def test_03_delete_university(self, headers, delete_university):
        uni_id = delete_university[0]
        get_deleted_uni = requests.get(
            config.BASE_URL + f"/university/{uni_id}",
            headers=headers,
        )
        with soft_assertions():
            assert_that(delete_university[1].status_code).is_equal_to(200)
            assert_that(get_deleted_uni.status_code).is_equal_to(404)

    def test_04_update_university(self, update_university, headers):
        uni_id = update_university[0]
        update_response = update_university[1]
        get_updated_uni = requests.get(
            config.BASE_URL + f"/university/{uni_id}", headers=headers
        )

        with soft_assertions():
            assert_that(update_response.status_code).is_equal_to(200)
            assert_that(get_updated_uni.json()["data"][0]["name"]).is_equal_to(
                "Updated name"
            )
