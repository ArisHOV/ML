from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import csv

class Persistor(ABC):




    def read_raw_data(self,path):
        with open(path,'r',encoding='utf-8') as file:
            data=file.read()
        soup = BeautifulSoup(data, 'html.parser')
        items = soup.find_all('div', class_='proposition')
        return items



    def save_raw_data(self, data,path):
        with open(path, "w", newline='', encoding='utf-8') as file:
            file.write(data)



    def save_csv(self, data,path):
        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'usd_price', 'transmission', 'city'])
            for dat in data:
                writer.writerow([dat.property_1, dat.property_2, dat.property_3, dat.property_4])


    def append_data(self, data):
        print("")
