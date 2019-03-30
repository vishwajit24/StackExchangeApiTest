import logging
import requests

logging.basicConfig(level=logging.INFO)


class StockExchangeAPIOperations(object):

    def __init__(self):
        self.url = 'http://api.stackexchange.com/2.2/'
        self.headers = {
            'Content-type': 'application/json',
        }
        self.site_name = 'stackoverflow'

    def get_tags(self, site_name=''):

        logger = logging.getLogger("get_tags")

        url = self.url + "tags"
        if site_name:
            site = site_name,
        else:
            site = self.site_name,
        payload = {
            'site': site
        }

        try:
            logger.info("Getting all the tags from site %s" % self.site_name)
            response = requests.get(url, params=payload, headers=self.headers)
            logger.info("Response content: %r", response.content)
            return response
        except Exception as e:
            logger.error("Error occurred while getting the pet entry %r" % e)
            raise e

    def get_tag_info(self, tag_name, site_name=''):

        logger = logging.getLogger("get_tag_info")

        url = self.url + "tags/{}/info".format(tag_name)

        if site_name:
            site = site_name,
        else:
            site = self.site_name,
        payload = {
            'site': site
        }

        try:
            logger.info("Getting the tag %s info from site %s" % (tag_name, self.site_name))
            response = requests.get(url, params=payload, headers=self.headers)
            logger.info("Response content: %r", response.content)
            return response
        except Exception as e:
            logger.error("Error occurred while getting the pet entry %r" % e)
            raise e

    def get_tag_for_moderator_only(self, site_name=''):

        logger = logging.getLogger("get_tag_for_moderator_only")

        url = self.url + "tags/moderator-only"

        if site_name:
            site = site_name,
        else:
            site = self.site_name,
        payload = {
            'site': site
        }

        try:
            logger.info("Getting the tag for moderator only from site %s" % self.site_name)
            response = requests.get(url, params=payload, headers=self.headers)
            logger.info("Response content: %r", response.content)
            return response
        except Exception as e:
            logger.error("Error occurred while getting the pet entry %r" % e)
            raise e

    def get_tag_required(self, site_name=''):

        logger = logging.getLogger("get_tag_required")

        url = self.url + "tags/required"

        if site_name:
            site = site_name,
        else:
            site = self.site_name,
        payload = {
            'site': site
        }

        try:
            logger.info("Getting the tag required from site %s" % self.site_name)
            response = requests.get(url, params=payload, headers=self.headers)
            logger.info("Response content: %r", response.content)
            return response
        except Exception as e:
            logger.error("Error occurred while getting the pet entry %r" % e)
            raise e

    def get_tag_synonyms(self, site_name=''):

        logger = logging.getLogger("get_tag_synonyms")

        url = self.url + "/tags/synonyms"

        if site_name:
            site = site_name,
        else:
            site = self.site_name,
        payload = {
            'site': site
        }

        try:
            logger.info("Getting the tag synonyms from site %s" % self.site_name)
            response = requests.get(url, params=payload, headers=self.headers)
            logger.info("Response content: %r", response.content)
            return response
        except Exception as e:
            logger.error("Error occurred while getting the pet entry %r" % e)
            raise e


StockExchangeAPIOperations().get_tags()