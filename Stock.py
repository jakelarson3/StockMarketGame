class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_owned = False
        self.percent_change = 0.0
        self.prices_log = []
        self.prices_log.append(self.price)

    def __str__(self):
        return self.name + ": " + self.price

    def get_name(self):
        """getter for stock name"""
        return self.name

    def get_price(self):
        """getter for stock price"""
        return self.price

    def set_price(self, new_price):
        """sets the stock price"""
        if new_price < 0:
            self.price = 0
            self.prices_log.append(self.price)
        else:
            self.price = new_price
            self.prices_log.append(self.price)

    def print_prev_prices(self):
        current_index = 0
        for stock in self.prices_log:
            print("Day %d: " % current_index)


