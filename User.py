class User:
    def __init__(self, name, money_amount):
        self.name = name
        self.money = float(money_amount)
        self.stocks = []

    def buy_stock(self, new_stock, quantity, offer_price):
        """for when a user wants to buy a stock"""
        if new_stock.is_owned:
            for stock in self.stocks:
                if new_stock.lower() == stock.name.lower():
                    stock.quantity_owned += quantity
        else:
            new_stock.is_owned = True
            new_stock.quantity_owned = quantity
            self.stocks.append(new_stock)
        self.money -= (offer_price * quantity)

    def sell_stock(self, stock_to_remove, quantity):
        """sells the stock that the user wants to sell"""
        for stock in self.stocks:
            if stock_to_remove == stock:
                if stock.quantity_owned > 1:
                    if quantity > stock.quantity_owned:
                        print("You do not own that much of the stock!")
                        return
                    elif quantity == stock.quantity_owned:
                        self.money += stock.price * quantity
                        self.stocks.remove(stock_to_remove)
                        stock_to_remove.not_owned_anymore()
                        return
                    else:
                        stock.quantity_owned -= quantity
                        self.money += stock.price * quantity
                        return
                elif stock.quantity_owned == 1:
                    if quantity > 1:
                        print("You do not own that much of the stock!")
                        return
                    else:
                        self.money += stock.price
                        self.stocks.remove(stock_to_remove)
                        stock_to_remove.not_owned_anymore()
                    return
        self.money += quantity  # transaction fee bonus!

    def stocks_to_string(self):
        """makes the user's owned stock into a string"""
        num_stocks = len(self.stocks)
        current_index = 0
        stocks_string = ""
        if len(self.stocks) == 0:
            #print("You don't own any stocks yet!")
            return
        for stock in self.stocks:
            if current_index == num_stocks - 1:  # don't print "," at end
                single_stock = stock.name + ' ($' + str(stock.price) + ')'
            else:
                single_stock = stock.name + ' ($' + str(stock.price) + '), '
            stocks_string += single_stock
            current_index += 1
        return stocks_string

    def display_net_worth(self):
        if len(self.stocks) == 0:
            return
        stock_worth = self.get_stock_worth()
        net_worth = self.money + stock_worth
        print("Your net worth is $" + str(round(net_worth, 2)))

    def display_cash(self):
        return "Cash Left: " + self.money

    def display_user(self):
        """displays the name, cash, and stocks the user has"""
        stock = self.stocks_to_string()
        if stock:
            str_to_print = "Name: " + self.name + "\nCash Left: $" + str(self.money) + "\nStocks: " + stock
        else:
            str_to_print = "Name: " + self.name + "\nCash Left: $" + str(self.money) + "\nStocks: None"
        print(str_to_print)

    def get_stock_worth(self):
        """returns the amount of money left + market price of the stocks the user owns"""
        stock_worth = 0.0
        for stock in self.stocks:
            current_worth = stock.price * stock.quantity_owned
            stock_worth += current_worth
        return round(stock_worth,2)

    def is_stock_owned(self, stock_to_check):
        """checks if user owns the inputted stock name string"""
        for stock in self.stocks:
            if stock_to_check == stock:
                return True
        return -1

    def can_user_afford(self, offer_price, quantity):
        """checks if the user has enough money to make a purchase"""
        if (offer_price * quantity) > self.money:
            return False
        else:
            return True

    def can_user_sell(self, stock_to_sell, quantity):
        """checks if the user has the stock and has enough quantity to sell it"""
        for stock in self.stocks:
            if stock_to_sell == stock:
                if quantity > stock.quantity_owned:
                    return False
                else:
                    return True

    def update_stocks(self, stock_market_stocks_list):
        """updates the current market values of the stock market to the users' stock list"""
        for stock in self.stocks:
            for market_stock in stock_market_stocks_list:
                if stock.name == market_stock.name:
                    stock.set_price(market_stock.price)








