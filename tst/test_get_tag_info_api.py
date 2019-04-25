import json
import random
import string
import pytest

from helpers.utils import tag_item_schema_validator, validate_response_for_invalid_site
from tst.stack_api_test import StackAPIBaseTest


class TestGetTagInfoAPI(StackAPIBaseTest):
    timeout = 60

    @pytest.mark.timeout(timeout)
    def test_tag_info_api_with_valid_tag_name(self):
        tag_info_response = self.stack_exchange.get_tags()
        tag_info_response = json.loads(tag_info_response.text)

        if len(tag_info_response['items']):
            tag_name = tag_info_response['items'][0]['name']

            response = self.stack_exchange.get_tag_info(tag_name=tag_name)
            assert response.status_code == 200
            response = json.loads(response.text)
            tag_item_schema_validator(response)
        else:
            pass

    @pytest.mark.timeout(timeout)
    def test_tag_info_api_with_invalid_tag_name(self):
        tag_name = self.get_test_data_for_tag_name()
        response = self.stack_exchange.get_tag_info(tag_name=tag_name)
        assert response.status_code == 200
        response = json.loads(response.text)
        tag_item_schema_validator(response)
        assert len(response['items']) == 0
        assert response['has_more'] == False

    @pytest.mark.timeout(timeout)
    def test_tag_required_info_with_invalid_site(self):
        site_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        tag_info_response = self.stack_exchange.get_tags()
        tag_info_response = json.loads(tag_info_response.text)

        if len(tag_info_response['items']):
            tag_name = tag_info_response['items'][0]['name']
            response = self.stack_exchange.get_tag_info(tag_name=tag_name, site_name=site_name)
            assert response.status_code == 400
            response = json.loads(response.text)
            validate_response_for_invalid_site(response, site_name)
        else:
            pass

