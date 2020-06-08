import logging
import requests



logger = logging.getLogger(__name__)


class Scraper:

    def __init__(self, storage):
        self.storage = storage

    def scrape(self,path):


        url = 'https://auto.ria.com/newauto/search/?page=1&markaId=47&size=100'
        headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
                 ,'accept': '*/*'}
        response = requests.get(url)

        if not response.ok:
            # log the error
            logger.error(response.text)

        else:
            # Note: here json can be used as response.json
            data = response.text

            # save scraped objects here
            # you can save url to identify already scrapped objects
            self.storage.save_raw_data(data,path)

