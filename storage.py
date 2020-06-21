from abc import ABC, abstractmethod

import csv

class Persistor(ABC):

    def read_raw_data(self,path):
        with open(path,'r',encoding='utf-8') as file:
            data=file.read()
        return data


    def save_raw_data(self, data,path):
        with open(path, "w", newline='', encoding='utf-8') as file:
            file.write(data)


    def save_csv(self, data,path):
        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'usd_price', 'transmission','motor','locationofengine'])
            for item in data:
                writer.writerow([item.title, item.price, item.transmission,item.motor,item.locationofengine])


    def append_data(self, data):
        print("")
