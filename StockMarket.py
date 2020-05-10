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
        for i in range(0,10):
            name_to_remove = random.choice(names)
            if i < 4:
                new_stock = Stock(name_to_remove, round(random.uniform(0,50), 2))
            elif 4 <= i < 8:
                new_stock = Stock(name_to_remove, round(random.uniform(51,150), 2))
            else:
                new_stock = Stock(name_to_remove, round(random.uniform(150,310), 2))
            names.remove(name_to_remove)
            self.stocks.append(new_stock)