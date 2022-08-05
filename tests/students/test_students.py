import pytest
import requests
from assertpy import assert_that, soft_assertions

import config


@pytest.mark.students
class TestStudents:
    def test_01_get_list_of_students_response_200(self, headers):
        student_list = requests.get(config.BASE_URL + "/student/", headers=headers)

        with soft_assertions():
            assert_that(student_list.status_code).is_equal_to(200)
            assert_that(student_list.json()["data"]).is_not_empty()

    def test_02_post_get_delete_flow(self, headers, student_data):
        new_student = requests.post(
            config.BASE_URL + "/student/",
            headers=headers,
            json=student_data,
        )
        assert_that(new_student.status_code).is_equal_to(200)
        student_id = new_student.json()["data"][0]["id"]
        get_student = requests.get(
            config.BASE_URL + f"/student/{student_id}", headers=headers
        )
        assert_that(get_student.status_code).is_equal_to(200)
        delete_student = requests.delete(
            config.BASE_URL + f"/student/{student_id}", headers=headers
        )
        assert_that(delete_student.status_code).is_equal_to(200)
        get_not_existing_student = requests.get(
            config.BASE_URL + f"/student/{student_id}", headers=headers
        )
        assert_that(get_not_existing_student.status_code).is_equal_to(404)
