from StockMarket import StockMarket
from User import User
import time
import threading

def main():
    #valid commands 
    running = True
    initialized = False
    stock_market = StockMarket()
    stock_market.create_stocks()
    while running:
        if not initialized:
            user = startup()
            initialized = True
        print("Enter 'view', 'buy', 'sell', 'advance', 'help' or 'exit':")
        try:
            user_in = input(":").lower()
            if user_in == "view":
                view(stock_market, user)
            elif user_in == "buy":
                buy(stock_market, user)
            elif user_in == "sell":
                sell(stock_market, user)
            elif user_in == "advance":
                stock_market.next_day()
                user.update_stocks(stock_market.stocks)
            elif user_in == "help":
                help_me()
            elif user_in == "exit":
                break
        except KeyboardInterrupt:
            break
    return "\nThank you for playing our stock market game!"

def help_me():
    print("Welcome to Stockify!\n\
This is a stock market game. You are in the main menu.\n\
Your options are to view, buy, or sell stocks.\n\
Enter either 'view', 'buy', or 'sell'.\n\
or enter 'exit' to stop the game or enter\n\
help if you want to see this lovely message again :)")
    return

def view(stock_market,user):
    print("Would you like to view your own stock or market stocks (enter 'my' or 'market' or 'back'):")
    user_in = input(":").lower()
    if user_in == 'my':
        user.display_user()
    elif user_in == 'market':
        for stock in stock_market.stocks:
            print(str(stock))
    elif user_in == "back":
        return ""
    else:
        print("invalid input")
        view(stock_market, user)
    return ""

def buy(stock_market, user):
    print("What company's stock would you like to buy?\n\
Your options are: 'Wonka Industries', 'Acme Corp.', 'Stark Industries',\n\
'Wayne Enterprises', 'Soylent', 'Hooli', 'Prestige Worldwide', 'Los Pollos Hermanos',\n\
'Oscorp', 'Iron Bank of Braavos'")
    user_in = input(":").lower()
    if user_in in [s.lower() for s in stock_market.stock_names]:
        for stock in stock_market.stocks:
            if user_in == stock.name.lower():
                stock_to_buy = stock
                print(str(stock))
        offers = stock_market.generate_offers(stock_to_buy)
        print("You have three offers that could be cheaper or more expensive than the current stock price\n\
1: %.2f, 2: %.2f, or 3: %.2f\n\
Enter the number of the price that you want to buy at('1', '2' or '3'):" % (offers[0], offers[1], offers[2]))
        while True:
            user_offer = input(":")
            if user_offer in ["1","2","3"]:
                offer_price = offers[int(user_offer)-1]
                break
            else:
                print("Invalid input")

        print("Enter the quantitiy of the stock you want(integer only): ")
        while True:
            user_amount = input(":")
            try:
                user_amount = int(user_amount)
                if user.can_user_afford(offer_price, user_amount):
                    #buy stock
                    user.buy_stock(stock_to_buy, user_amount, offer_price)
                    print("Stock purchased")
                    break
                else:
                    print("You can not afford that, try again")
                    raise ValueError
            except ValueError:
                print("Invalid input")
    elif user_in == "back":
        pass
    else:
        print("invalid input")
        buy(stock_market,user)
    return ""

def sell():
    return ""

def startup():
    #initialize the stock market game
    #will return with initial money count and user name
    print("Hello, welcome to the stock market game!\n\
This game consists of buying and selling stock with\n\
the purpose of simulating the real stock market.\n\n\
In this game the stocks are simulations of a real\n\
stock market however, there are fictionalized busts\n\
and booms. So try not to lose everything or if you do,\n\
just restart :)      Good Luck!\n")
    while True:
        name = input("Please enter a nickname: ")
        if name.isalpha() and 0 < len(name) < 20:
            break
        else:
            print("Invalid name")
    while True:
        init_money = input("Please enter starting cash amount(100-10,000): ")
        if init_money.isdigit() and 2 < len(init_money) < 5:
            break
        else:
            print("Invalid amount")
    user = User(name, init_money)
    return user

if __name__ == "__main__":
    print(main())