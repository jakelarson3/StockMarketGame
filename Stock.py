class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_owned = False
        self.percent_change = 0.0
        self.prices_log = []
        self.prices_log.append(self.price)

    def __str__(self):
        """returns the string of the stock name and price"""
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
        """prints the list of the stock prices that the stock has previously had"""
        current_index = 0
        for stock in self.prices_log:
            str_to_print = "Day {0}: {1}".format(current_index, self.prices_log[current_index])
            print(str_to_print)
            current_index += 1


