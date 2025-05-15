# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        self._price = val
        print("Price updated...")

    @price.deleter
    def price(self):
        del self._price
        print("Price deleted")

        


d = Product(3000)

print(d.price)

d.price = 3400

print(d.price)

del d.price

