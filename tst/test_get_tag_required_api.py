import pytest
import json
import random
import string

from stackexchange_api_operations.stock_exchange_api_operations import StockExchangeAPIOperations
from tst.utils import tag_schema_validator, check_if_element_is_present_in_response, ordered, \
    validate_response_for_invalid_site

stockExchange = StockExchangeAPIOperations()


@pytest.mark.timeout(60)
def test_tag_required_api_schema():
    response = stockExchange.get_tag_required()
    assert response.status_code == 200
    response = json.loads(response.text)
    tag_schema_validator(response)


@pytest.mark.timeout(60)
def test_tag_required_api_data():
    tag_info_response = stockExchange.get_tags()
    tag_info_response = json.loads(tag_info_response.text)

    tag_required_response = stockExchange.get_tag_required()
    assert tag_required_response.status_code == 200
    tag_required_response = json.loads(tag_required_response.text)

    item = check_if_element_is_present_in_response('is_required', tag_info_response)
    if len(item):
        assert len(tag_required_response['items']) == 0
    else:
        assert ordered(item) == ordered(tag_required_response['items'])


@pytest.mark.timeout(60)
def test_tag_required_info_with_invalid_site():
    site_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    response = stockExchange.get_tag_required(site_name=site_name)
    assert response.status_code == 400
    response = json.loads(response.text)
    validate_response_for_invalid_site(response, site_name)


