import random
from Stock import Stock


class StockMarket:
    def __init__(self):
        self.max_days = 10
        self.current_day = 0
        self.dow = 0.0
        self.stocks = []
        self.is_market_crash = False
        self.is_market_boom = False

    def create_stocks(self):
        """creates the stocks that are going to be used in the stock market game"""
        names = ['Wonka Industries','Acme Corp.', 'Stark Industries', 'Wayne Enterprises', 'Soylent', 'Hooli', 'Prestige Worldwide',
         'Los Pollos Hermanos', 'Oscorp', 'Iron Bank of Braavos']
        for i in range(0, 10):
            name_to_remove = random.choice(names)
            if i < 4:
                new_stock = Stock(name_to_remove, round(random.uniform(2, 50), 2))
            elif 4 <= i < 8:
                new_stock = Stock(name_to_remove, round(random.uniform(51, 150), 2))
            else:
                new_stock = Stock(name_to_remove, round(random.uniform(150, 310), 2))
            names.remove(name_to_remove)
            self.stocks.append(new_stock)

    def next_day(self):
        """updates the day of the stock market"""
        # call randomize stock prices
        self.current_day += 1


    def overnight_stock_update(self):
        """updates the stock price of each stock by a (semi) random amount"""
        if self.is_market_boom:
            self.boom_stock_update()
        elif self.is_market_crash:
            self.crash_stock_update()
        else:  # is a regular day
            self.regular_stock_update()

    def regular_stock_update(self):
        """updates the stock price overnight for a regular market"""
        for stock in self.stocks:
            random_chance = random.random()
            if stock.price <= 10:  # small company
                if 0.0 < random_chance <= 0.75:
                    change_percent = random.uniform(.2, 3)
                    stock.set_price(stock.price * change_percent)
                else:  # small stock increases fast
                    change_percent = random.uniform(5, 15)
                    stock.set_price(stock.price * change_percent)
            elif 10 < stock.price <= 50:  # medium company
                if 0.0 < random_chance <= 0.75:
                    change_percent = random.uniform(.6, 1.4)
                    stock.set_price(stock.price * change_percent)
                else:  # medium stock increases slightly better than normal
                    change_percent = random.uniform(1.5, 3)
                    stock.set_price(stock.price * change_percent)
            elif 50 < stock.price <= 150:  # medium large company
                if 0.0 < random_chance <= 0.85:
                    change_percent = random.uniform(.85, 1.15)
                    stock.set_price(stock.price * change_percent)
                else:  # medium stock increases slightly better than normal
                    change_percent = random.uniform(1.15, 1.3)
                    stock.set_price(stock.price * change_percent)
            else:  # very large company
                if 0.0 < random_chance <= 0.95:
                    change_percent = random.uniform(.95, 1.05)
                    stock.set_price(stock.price * change_percent)
                else:  # medium stock increases slightly better than normal
                    change_percent = random.uniform(1.05, 1.15)
                    stock.set_price(stock.price * change_percent)

    def boom_stock_update(self):
        """updates the stock price overnight for a regular market"""
        for stock in self.stocks:
            random_chance = random.random()
            if stock.price <= 10:  # small company
                if 0.0 < random_chance <= 0.65:
                    change_percent = random.uniform(.9, 10)
                    stock.set_price(stock.price * change_percent)
                else:  # small stock increases fast
                    change_percent = random.uniform(10, 20)
                    stock.set_price(stock.price * change_percent)
            elif 10 < stock.price <= 50:  # medium company
                if 0.0 < random_chance <= 0.85:
                    change_percent = random.uniform(.9, 2)
                    stock.set_price(stock.price * change_percent)
                else:  # medium stock increases slightly better than normal
                    change_percent = random.uniform(2, 4)
                    stock.set_price(stock.price * change_percent)
            elif 50 < stock.price <= 150:  # medium large company
                if 0.0 < random_chance <= 0.85:
                    change_percent = random.uniform(.95, 1.20)
                    stock.set_price(stock.price * change_percent)
                else:  # medium stock increases slightly better than normal
                    change_percent = random.uniform(1.2, 1.4)
                    stock.set_price(stock.price * change_percent)
            else:  # very large company
                if 0.0 < random_chance <= 0.95:
                    change_percent = random.uniform(1, 1.08)
                    stock.set_price(stock.price * change_percent)
                else:  # medium stock increases slightly better than normal
                    change_percent = random.uniform(1.08, 1.2)
                    stock.set_price(stock.price * change_percent)

    def crash_stock_update(self):
        """updates the stock price overnight for a regular market"""
        for stock in self.stocks:
            random_chance = random.random()
            if stock.price <= 10:  # small company
                if 0.0 < random_chance <= 0.65:
                    change_percent = random.uniform(0.2, 2)
                    stock.set_price(stock.price * change_percent)
                else:  # small stock increases fast
                    change_percent = random.uniform(0.01, 1)
                    stock.set_price(stock.price * change_percent)
            elif 10 < stock.price <= 50:  # medium company
                if 0.0 < random_chance <= 0.85:
                    change_percent = random.uniform(.6, 1.5)
                    stock.set_price(stock.price * change_percent)
                else:  # medium stock increases slightly better than normal
                    change_percent = random.uniform(0.2, 1)
                    stock.set_price(stock.price * change_percent)
            elif 50 < stock.price <= 150:  # medium large company
                if 0.0 < random_chance <= 0.85:
                    change_percent = random.uniform(.6, 1.10)
                    stock.set_price(stock.price * change_percent)
                else:  # medium stock increases slightly better than normal
                    change_percent = random.uniform(.4, 1)
                    stock.set_price(stock.price * change_percent)
            else:  # very large company
                if 0.0 < random_chance <= 0.95:
                    change_percent = random.uniform(.8, 1.03)
                    stock.set_price(stock.price * change_percent)
                else:  # medium stock increases slightly better than normal
                    change_percent = random.uniform(.7, 1)
                    stock.set_price(stock.price * change_percent)









