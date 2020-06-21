import logging
import requests



logger = logging.getLogger(__name__)


class Scraper:

    def __init__(self, storage):
        self.storage = storage

    def scrape(self,path):
        url = 'https://auto.ria.com/newauto/search/?page=1&markaId=47&size=100'
        response = requests.get(url)
        if not response.ok:
            logger.error(response.text)
        else:
            data = response.text
            self.storage.save_raw_data(data,path)
   #gathered html file from the internet and save this html file
