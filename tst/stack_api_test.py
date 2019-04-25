import json
import random

from stackexchange_api_operations.stack_exchange_api_operations import StackExchangeAPIOperations


class StackAPIBaseTest(object):
    stack_exchange = None
    test_data_file = ''

    def setup_method(self, method):
        self.stack_exchange = StackExchangeAPIOperations()
        self.test_data_file = "../helpers/" + "test_data"

    def get_test_data_for_site_name(self):
        with open(self.test_data_file) as json_file:
            data = json.load(json_file)

            site_name = data['site_name']
            return random.choice(site_name)

    def get_test_data_for_tag_name(self):
        with open(self.test_data_file) as json_file:
            data = json.load(json_file)

            tag_name = data['tag_name']
            return random.choice(tag_name)

    def get_test_timeout(self):
        with open(self.test_data_file) as json_file:
            data = json.load(json_file)
            return data['test_timeout']





