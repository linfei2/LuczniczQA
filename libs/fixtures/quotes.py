import pytest
import requests
from assertpy import assert_that

import config


@pytest.fixture
def create_and_delete_quote():
    quote = requests.post(
        config.BASE_URL + "/quote/",
        headers=config.BASE_HEADERS,
        json={"quote": "Tekst cytatu", "author": "Autor cytatu"},
    )

    assert_that(quote.status_code).is_equal_to(200)
    quote_id = quote.json()["data"][0]["id"]
    quote_data = quote.json()
    yield quote_id, quote_data
    delete_quote = requests.delete(
        config.BASE_URL + f"/quote/{quote_id}", headers=config.BASE_HEADERS
    )
    assert_that(delete_quote.status_code).is_equal_to(200)
