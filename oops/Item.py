import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity=0):
        assert price > 0, f"price {price} can't be zero or negative"
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as my_file:
            reader = csv.DictReader(my_file)
            items = list(reader)
        for item in items:
            Item(
                name= item.get('name'),
                price= int(item.get('price')),
                quantity= item.get('quantity')
            )

    @staticmethod
    def check_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False



    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name} is product type"


item1 = Item("Phone", -100, 20)
item2 = Item("Laptop", 1000, 5)
# item3 = Item("Cable", 20, 30)
# item4 = Item("Mouse", 50, 40)
# item5 = Item("Keyboard", 30, 60)
# print(item1)
# print(item1.apply_discount())
# print(item1.price)
# item2.has_num_pad = False
# print(Item.all)
#
Item.instantiate_from_csv()
items = Item.all

for item in items:
    if item.name == "Laptop":
        # item.apply_discount()
        print(item.price)

#
# print(Item.check_integer(10))
