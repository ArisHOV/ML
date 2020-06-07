from object import Item


class Parser:

    def parse_object(self, content):

        return Item(
            property_1=self.get_property_1(content),
            property_2=self.get_property_2(content),
            property_3=self.get_property_3(content),
            property_4=self.get_property_4(content)

        )

    def get_property_1(self, content):
        return  content.find('h3',class_='proposition_name').get_text(strip=True)

    def get_property_2(self, content):
        return content.find('span',class_='green').get_text(strip=True)

    def get_property_3(self, content):
        return content.find('div',class_='proposition_information').find_all('span',class_='size13')[1].get_text(strip=True)

    def get_property_4(self, content):
        return content.find('svg', class_='svg svg-i16_pin').find_next('strong').get('title')


