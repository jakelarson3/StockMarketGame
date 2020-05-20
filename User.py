from Stock import Stock

class User:
    def __init__(self, name, money_amount):
        self.name = name
        self.money = money_amount
        self.stocks = []

    def buy_stock(self, new_stock, quantity, offer_price):
        """for when a user wants to buy a stock"""
        if new_stock.is_owned:
            for stock in self.stocks:
                if new_stock.name == stock.name:
                    stock.quantity_owned += quantity
        else:
            new_stock.is_owned = True
            self.stocks.append(new_stock)
        self.money -= (offer_price * quantity)

    def sell_stock(self, stock_to_remove, quantity):
        for stock in self.stocks:
            if stock.name.lower() == stock_to_remove.lower():
                if stock.quantity_owned > 1:
                    if quantity == stock.quantity_owned:
                        self.money += stock.price * quantity
                        self.stocks.remove(stock)
                    else:
                        stock.quantity_owned -= quantity
                        self.money += stock.price * quantity
                elif stock.quantity_owned == 1:
                    self.money += stock.price
                    self.stocks.remove(stock)

        self.money += quantity  # transaction fee bonus!

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

    def spend_money(self, price):
        self.money -= price

    def display_user(self):
        stock = self.stocks_to_string()
        str_to_print = "Name: " + self.name + "\nCash Left: " + str(self.money) + "\nStocks: " + stock
        print(str_to_print)

    def get_total_worth(self):
        """returns the amount of money left + market price of the stocks the user owns"""
        stock_worth = 0.0
        for stock in self.stocks:
            current_worth = stock.price * stock.quantity_owned
            stock_worth += current_worth
        return stock_worth




