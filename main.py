"""

Your task is to gather data from the Internet,
parse it and save to a csv file

To run the file you can use your ide or terminal:
python3 -m main gather
python3 -m main parse

The logging package helps you to better track how the processes work
It can also be used for saving the errors that arise

"""

import sys
import logging

from scraper import Scraper
from parse import Parser
from storage import Persistor
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SCRAPPED_FILE = 'scrapped_data.txt'
TABLE_FORMAT_FILE = 'data.csv'


def gather():
    logger.info("gather")
    storage = Persistor()

    scrapper = Scraper(storage)
    scrapper.scrape(SCRAPPED_FILE)


def parse():

    logger.info("parse")
    storage = Persistor()
    parser = Parser()

    raw_data = storage.read_raw_data(SCRAPPED_FILE)
    parsed_files = [parser.parse_object(file) for file in raw_data]
    storage.save_csv(parsed_files,TABLE_FORMAT_FILE)


def stats():
    logger.info("stats")
    # Your code here
    # Load pandas DataFrame and print to stdout different statistics about the data.
    # Try to think about the data and use as different methods applicable to DataFrames.
    # Ask yourself what would you like to know about this data (most frequent word, average price, e.t.c.)


if __name__ == '__main__':

    logger.info("Work started")
    sys.argv[0]='gather'

    if sys.argv[0] == 'gather':
        gather()

    elif sys.argv[0] == 'parse':
        parse()

    logger.info("work ended")
