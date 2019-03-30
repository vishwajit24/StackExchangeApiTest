import pytest
import json
import random
import string

from stackexchange_api_operations.stock_exchange_api_operations import StockExchangeAPIOperations
from tst.utils import tag_schema_validator, check_if_element_is_present_in_response, ordered

stockExchange = StockExchangeAPIOperations()


@pytest.mark.timeout(60)
def test_tag_moderator_only_api():
    response = stockExchange.get_tag_for_moderator_only()
    assert response.status_code == 200
    response = json.loads(response.text)
    tag_schema_validator(response)


@pytest.mark.timeout(60)
def test_tag_moderator_only_api_data():
    tag_info_response = stockExchange.get_tags()
    tag_info_response = json.loads(tag_info_response.text)

    tag_moderator = stockExchange.get_tag_for_moderator_only()
    assert tag_moderator.status_code == 200
    tag_moderator = json.loads(tag_moderator.text)

    item = check_if_element_is_present_in_response('is_moderator_only', tag_info_response)
    if len(item):
        assert len(tag_moderator['items']) == 0
    else:
        assert ordered(item) == ordered(tag_moderator['items'])


@pytest.mark.timeout(60)
def test_tag_required_info_with_invalid_site():
    site_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    response = stockExchange.get_tag_for_moderator_only(site_name=site_name)
    assert response.status_code == 400
    response = json.loads(response.text)
    print(response)

