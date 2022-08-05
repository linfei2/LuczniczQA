from datetime import timedelta

import pytest
import requests
from assertpy import assert_that, soft_assertions


@pytest.mark.quote
@pytest.mark.usefixtures("create_and_delete_quote")
class TestQuotes:
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    def test_01_get_quotes(self):
        response = requests.get("http://127.0.0.1:8080/quote/", headers=self.headers)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.json()["message"]).is_equal_to(
                "Quotes data retrieved successfully"
            )
            assert_that(response.json()["data"]).is_not_empty()
            assert_that(response.json()["data"][0][0]["id"]).is_not_empty()
            assert_that(response.json()["data"][0][0]).contains_key("quote")
            assert_that(response.json()["data"][0][0]).contains_key("author")
            assert_that(response.headers).contains("x-luczniczqa")
            assert_that(response.headers["server"]).is_equal_to("uvicorn")

    def test_02_update_quote_response_200(self, create_and_delete_quote):
        quote_id = create_and_delete_quote[0]
        update_quote = requests.put(
            f"http://127.0.0.1:8080/quote/{quote_id}",
            headers=self.headers,
            json={"quote": "Tekst innego cytatu", "author": "Inny autor"},
        )
        with soft_assertions():
            assert_that(update_quote.status_code).is_equal_to(200)
            assert_that(update_quote.json()["data"][0]).contains(quote_id)

        get_quote = requests.get(
            f"http://127.0.0.1:8080/quote/{quote_id}",
            headers=self.headers,
        )
        with soft_assertions():
            assert_that(get_quote.status_code).is_equal_to(200)
            assert_that(get_quote.json()["data"][0]["id"]).contains(quote_id)
            assert_that(get_quote.json()["data"][0]["quote"]).is_equal_to(
                "Tekst innego cytatu"
            )
            assert_that(get_quote.json()["data"][0]["author"]).is_equal_to("Inny autor")
            assert_that(get_quote.elapsed).is_less_than_or_equal_to(
                timedelta(milliseconds=500)
            )
