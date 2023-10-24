from oops.Item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, broken_phones):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

phone1 = Phone("iPhone12", 800, 5, 1)
phone2 = Phone("iphone13", 900, 8, 2)

# print(phone1.calculate_total_price())

