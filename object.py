class Item:

    def __init__(self, title=None, price=None, transmission=None,
                 ):
        self.title = title
        self.price = price
        self.transmission = transmission



    def __str__(self):
        return f'You can change what you want to see in the object, ' \
                f'when you print it, say its first property: {self.property_1}'