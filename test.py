class Order:
    def __init__(self, item, pieces, price, options):
        self.item = item
        self.pieces = pieces
        self.price = price
        self.options = options

    def total_price(self, pieces, price):
        total = pieces * price

