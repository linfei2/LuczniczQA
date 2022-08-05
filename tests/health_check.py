import pytest
import requests
from assertpy import assert_that, soft_assertions

import config


@pytest.mark.admin
class TestAnyEndpoint:
    def test_01_get_root_response_200(self):
        response = requests.get(
            config.BASE_URL,
            headers=config.BASE_HEADERS,
        )

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.json()["message"]).contains("API Testing app")
