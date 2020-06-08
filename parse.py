from object import Item


class Parser:

    def parse_object(self, content):

        return Item(
            title=self.get_title(content),
            price=self.get_price(content),
            transmission=self.get_transmission(content),


        )

    def get_title(self, content):
        return  content.find('h3',class_='proposition_name').get_text(strip=True)

    def get_price(self, content):
        return content.find('span',class_='green').get_text(strip=True)

    def get_transmission(self, content):
        return content.find('div',class_='proposition_information').find_all('span',class_='size13')[1].get_text(strip=True)




