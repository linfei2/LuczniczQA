import pytest
import requests

from assertpy import assert_that


@pytest.fixture
def create_and_delete_quote():
    quote = requests.post("http://127.0.0.1:8080/quote/",
                          headers={
                              "accept": "application/json",
                              "Content-Type": "application/json"
                          },
                          json={
                              "quote": "Tekst cytatu",
                              "author": "Autor cytatu"
                          })

    assert_that(quote.status_code).is_equal_to(200)
    quote_id = quote.json()["data"][0]["id"]
    quote_data = quote.json()
    yield quote_id, quote_data
    delete_quote = requests.delete(f"http://127.0.0.1:8080/quote/{quote_id}",
                                   headers={
                                       "accept": "application/json",
                                   })
    assert_that(delete_quote.status_code).is_equal_to(200)
