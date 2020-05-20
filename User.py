class User:
    def __init__(self):
        self.name = ""
        self.money = 1000
        self.stocks = []

    def change_name(self, name):
        self.name = name

    def add_stocks(self, new_stock):
        self.stocks.append(new_stock)

    def add_money(self, new_money):
        self.money += new_money

    def stocks_to_string(self):
        stocks_string = ""
        for i in self.stocks:
            stocks_string += self.stocks.name[i]

    def remove_stock(self, stock):
        for i in self.stocks:
            if self.stocks.name[i] == stock:
                self.stocks.pop(i)

    def spend_money(self, price):
        self.money -= price

    def display_user(self):
        stock = self.stocks_to_string()
        str = "Name: " + self.name + "\n Money: " + str(self.money) + "\n Stocks: " + stock


