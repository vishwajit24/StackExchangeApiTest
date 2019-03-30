import pytest
import json
import random
import string

from stackexchange_api_operations.stock_exchange_api_operations import StockExchangeAPIOperations
from tst.utils import validate_response_for_invalid_site, tag_schema_validator

stockExchange = StockExchangeAPIOperations()


@pytest.mark.timeout(60)
def test_tag_synonyms_api_schema():
    response = stockExchange.get_tag_synonyms()
    assert response.status_code == 200
    response = json.loads(response.text)
    tag_schema_validator(response)


@pytest.mark.timeout(60)
def test_tag_info_with_invalid_site():
    site_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    response = stockExchange.get_tag_synonyms(site_name=site_name)
    assert response.status_code == 400
    response = json.loads(response.text)
    validate_response_for_invalid_site(response, site_name)

