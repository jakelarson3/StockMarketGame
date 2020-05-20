from Stock import Stock

class User:
    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.stocks = []

    def add_stock(self, new_stock):
        if new_stock
        if new_stock.is_owned:
            for stock in self.stocks:


        self.stocks.append(new_stock)

    def stocks_to_string(self):
        num_stocks = len(self.stocks)
        current_index = 0
        stocks_string = ""
        if len(self.stocks) == 0:
            print("You don't own any stocks yet!")
            return
        for stock in self.stocks:
            if current_index == num_stocks - 1:  # don't print , at end
                single_stock = stock.name
            else:
                single_stock = stock.name + ', '
            stocks_string += single_stock
        return stocks_string

    def remove_stock(self, stock_to_remove):
        current_index = 0
        for stock in self.stocks:
            if stock.name == stock_to_remove:
                self.stocks.pop(current_index)
                break
            current_index += 1

    def spend_money(self, price):
        self.money -= price

    def display_user(self):
        stock = self.stocks_to_string()
        str_to_print = "Name: " + self.name + "\n Cash Left: " + str(self.money) + "\n Stocks: " + stock
        print(str_to_print)

    def get_total_worth(self):
        """returns the amount of money left + market price of the stocks the user owns"""
        stock_worth = 0.0
        for stock in self.stocks:
            current_worth = stock.price * stock.quantity_owned
            stock_worth += current_worth
        return stock_worth




