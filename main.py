"""

I decided to parse Mazda brand cars their year, price and transmission

"""

import sys
import logging

from scraper import Scraper
from parse import Parser
from storage import Persistor
import pandas as pd



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
    cars=pd.read_csv('data.csv')
    mean=meanofprice(converttoint(cars['usd_price']))
    print(f'mean of price: {mean}')



def converttoint(prices):
    car=[]
    for price in prices:
        car.append(int(price.replace('$','').replace(' ','')))
    return car

def meanofprice(prices):
    s=0
    for price in prices:
        s+=price
    s/= len(prices)
    return s


if __name__ == '__main__':

    logger.info("Work started")
    #sys.argv[0]='stats'

    if sys.argv[0] == 'gather':
        gather()

    elif sys.argv[0] == 'parse':
        parse()
    elif sys.argv[0]=='stats':
        stats()

    logger.info("work ended")
