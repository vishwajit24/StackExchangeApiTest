import json
import pytest

from helpers.utils import tag_item_schema_validator, validate_response_for_invalid_site
from tst.stack_api_test import StackAPIBaseTest


class TestGetTagsAPI(StackAPIBaseTest):
    timeout = 60

    @pytest.mark.timeout(timeout)
    def test_tag_info(self):
        site_name = self.get_test_data_for_site_name()
        response = self.stack_exchange.get_tags(site_name)
        if response.status_code == 200:
            response = json.loads(response.text)
            tag_item_schema_validator(response)
        else:
            assert response.status_code == 400
            response = json.loads(response.text)
            validate_response_for_invalid_site(response, site_name)


