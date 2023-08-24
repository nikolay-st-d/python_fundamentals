class Item:
    def __int__(self, name):
        self.name = name

    def price(self, price, quantity):
        price = self.price * self.quantity
        return price


