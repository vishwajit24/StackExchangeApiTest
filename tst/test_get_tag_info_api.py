import pytest
import json
import random
import string

from stackexchange_api_operations.stock_exchange_api_operations import StockExchangeAPIOperations
from tst.utils import tag_schema_validator, \
    validate_response_for_invalid_site

stockExchange = StockExchangeAPIOperations()


@pytest.mark.timeout(60)
def test_tag_info_api_with_valid_tag_name():
    tag_info_response = stockExchange.get_tags()
    tag_info_response = json.loads(tag_info_response.text)

    if len(tag_info_response['items']):
        tag_name = tag_info_response['items'][0]['name']

        response = stockExchange.get_tag_info(tag_name=tag_name)
        assert response.status_code == 200
        response = json.loads(response.text)
        tag_schema_validator(response)
    else:
        pass


@pytest.mark.timeout(60)
def test_tag_info_api_with_invalid_tag_name():
    tag_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

    response = stockExchange.get_tag_info(tag_name=tag_name)
    assert response.status_code == 200
    response = json.loads(response.text)
    tag_schema_validator(response)
    assert len(response['items']) == 0
    assert response['has_more'] == False


@pytest.mark.timeout(60)
def test_tag_required_info_with_invalid_site():
    tag_name = ''
    site_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    tag_info_response = stockExchange.get_tags()
    tag_info_response = json.loads(tag_info_response.text)

    if len(tag_info_response['items']):
        tag_name = tag_info_response['items'][0]['name']
        response = stockExchange.get_tag_info(tag_name=tag_name, site_name=site_name)
        assert response.status_code == 400
        response = json.loads(response.text)
        validate_response_for_invalid_site(response, site_name)
    else:
        pass

