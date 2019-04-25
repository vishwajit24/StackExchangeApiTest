import json
import pytest

from helpers.utils import tag_item_schema_validator, check_if_element_is_present_in_response, ordered, \
    validate_response_for_invalid_site
from tst.stack_api_test import StackAPIBaseTest


class TestGetTagForModeratorOnly(StackAPIBaseTest):

    timeout = 60

    @pytest.mark.timeout(timeout)
    def test_tag_moderator_only_api(self):
        site_name = self.get_test_data_for_site_name()
        response = self.stack_exchange.get_tag_for_moderator_only(site_name)
        if response.status_code == 200:
            response = json.loads(response.text)
            tag_item_schema_validator(response)
        else:
            assert response.status_code == 400
            response = json.loads(response.text)
            validate_response_for_invalid_site(response, site_name)

    @pytest.mark.timeout(timeout)
    def test_tag_moderator_only_api_data(self):
        tag_info_response = self.stack_exchange.get_tags()
        tag_info_response = json.loads(tag_info_response.text)

        tag_moderator = self.stack_exchange.get_tag_for_moderator_only()
        assert tag_moderator.status_code == 200
        tag_moderator = json.loads(tag_moderator.text)

        item = check_if_element_is_present_in_response('is_moderator_only', tag_info_response)
        if len(item):
            assert len(tag_moderator['items']) == 0
        else:
            assert ordered(item) == ordered(tag_moderator['items'])



