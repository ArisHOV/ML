class Item:

    def __init__(self, title=None, price=None, transmission=None,motor=None,locationofengine=None
                 ):
        self.title = title
        self.price = price
        self.transmission = transmission
        self.motor=motor
        self.locationofengine=locationofengine


    def __str__(self):
        return f'You can change what you want to see in the object, ' \
                f'when you print it, say its first property: {self.property_1}'