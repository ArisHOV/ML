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
    data=parser.process_rawdata(raw_data)  #processing raw data
    parsed_files = [parser.parse_object(file) for file in data] #parsing every object
    storage.save_csv(parsed_files,TABLE_FORMAT_FILE) #save our data


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
#our price in data is not int so converting type int    

def meanofprice(prices):
    s=0
    for price in prices:
        s+=price
    s/= len(prices)
    return s
#mean of price every car that have on data


if __name__ == '__main__':

    logger.info("Work started")
    #sys.argv[0]='stats'

    if sys.argv[1] == 'gather':
        gather()

    elif sys.argv[1] == 'parse':
        parse()
    elif sys.argv[1]=='stats':
        stats()

    logger.info("work ended")
