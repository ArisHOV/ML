from object import Item
from bs4 import BeautifulSoup


class Parser:

    def parse_object(self, content):

        return Item(
            title=self.get_title(content),
            price=self.get_price(content),
            transmission=self.get_transmission(content),
            motor=self.get_motor(content),
            locationofengine=self.get_locationofengine(content)

        )

    def get_title(self, content):
        return  content.find('h3',class_='proposition_name').get_text(strip=True)
    #get title of car

    def get_price(self, content):
        return content.find('span',class_='green').get_text(strip=True)
     #get price of car
    def get_transmission(self, content):
        return content.find('div',class_='proposition_information').find_all('span',class_='size13')[1].get_text(strip=True)
    #get transmission of car
    def get_motor(self,content):
        return content.find('div',class_='proposition_information').contents[0].text
    # get motor of car
    def get_locationofengine(self,content):
        return content.find('div',class_='proposition_information').contents[8].text

    def process_rawdata(self,data):
        soup = BeautifulSoup(data, 'html.parser')
        items = soup.find_all('div', class_='proposition')
        return items
# processing raw data

