# import abc
from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name):
        self._name = name
        self._cart = []

    # blueprint for a purchase, can't instantiate, but a blueprint for every class that inherit's the Person class
    @abstractmethod
    def purchase(self, item, quantity):
        return

    def get_name(self):
        return self._name

    def get_cart(self):
        return self._cart

    def show_cart_total(self):
        total = 0
        for item, quantity in self._cart:
            total += item.get_price() * quantity
        return f"{total:.2f}"


# Dealer class inherits from Person class
class Dealer(Person):

    def __init__(self, name, discount):
        super().__init__(name)
        self._discount = discount

    def purchase(self, item, quantity):
        item.discount(self._discount)
        self._cart.append([item, quantity])


# Retail_Customer class inherits from Person class
class Retail_Customer(Person):

    def purchase(self, item, quantity):
        # look for the cart within the Person class
        self._cart.append([item, quantity])


class Item():

    def __init__(self, name, price):
        self._name = name
        self._price = price

    def discount(self, percentage_off):
        self._price *= (100 - percentage_off) / 100
        self._price = round(self._price, 2)

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price


# testing the program

# create an instance of Retail_Customer()
robbie = Retail_Customer('Robbie')
print(robbie.get_name())

# create items
teddyBear = Item('Teddy Bear', 24.99)
teddyBear2 = Item('Teddy Bear', 24.99)
rose = Item('Rose', 1.99)

# create an instance of Dealer() | Instace of dealer gets 25% off
jaren = Dealer("Jaren", 25)
print(jaren.get_name())

# jaren purchases
jaren.purchase(teddyBear, 2)
print(jaren._cart)

# robbie purchases
robbie.purchase(teddyBear2, 2)
# robbie.purchase(rose, 24)

# get cart from Jaren, the Dealer() and Robbie, the Retail_Customer()
print(jaren.get_cart())
print(robbie.get_cart())
# get cart total price from Jaren, the Dealer() and Robbie, the Retail_Customer()
print(robbie.show_cart_total())
print(jaren.show_cart_total())
