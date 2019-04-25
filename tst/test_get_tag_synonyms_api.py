import json
import pytest

from helpers.utils import validate_response_for_invalid_site, tag_schema_validator_for_synonyms
from tst.stack_api_test import StackAPIBaseTest


class TestGetTagSynonymsAPI(StackAPIBaseTest):
    timeout = 60

    @pytest.mark.timeout(timeout)
    def test_tag_synonyms_api_schema(self):
        site_name = self.get_test_data_for_site_name()
        response = self.stack_exchange.get_tag_synonyms(site_name)
        if response.status_code == 200:
            response = json.loads(response.text)
            tag_schema_validator_for_synonyms(response)
        else:
            assert response.status_code == 400
            response = json.loads(response.text)
            validate_response_for_invalid_site(response, site_name)

