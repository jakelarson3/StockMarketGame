class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_owned = False
        self.prices_log = []
        self.prices_log.append(self.price)
        self.quantity_owned = 0

    def __str__(self):
        """returns the string of the stock name and price"""
        return self.name + ": $" + str(self.price) + " Quantity Owned: " + str(self.quantity_owned)

    def __eq__(self, other):
        if self.name.lower() == other.name.lower():
            return True
        else:
            return False

    def get_name(self):
        """getter for stock name"""
        return self.name

    def get_price(self):
        """getter for stock price"""
        return self.price

    def set_price(self, new_price):
        """sets the stock price"""
        self.price = new_price
        self.prices_log.append(self.price)

    def print_prev_prices(self):
        """prints the list of the stock prices that the stock has previously had"""
        current_index = 0
        for stock in self.prices_log:
            str_to_print = "Day {0}: {1}".format(current_index, self.prices_log[current_index])
            print(str_to_print)
            current_index += 1

    def add_quantity(self, quantity):
        """adds a quantity of the current stock"""
        self.quantity_owned += quantity

    def has_been_bought(self):
        """changes the state of the stock to owned"""
        if self.is_owned:
            print("Already owned!")
            return
        else:
            self.is_owned = True

    def not_owned_anymore(self):
        """changes the state of the stock to not owned"""
        if not self.is_owned:
            print("Already not owned!")
            return
        else:
            self.is_owned = False





