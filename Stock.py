class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_owned = False
        self.percent_change = 0.0

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price
