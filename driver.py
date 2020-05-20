from Stock import Stock
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
            thread = threading.Thread(target = timer, kwargs = {"stocks" :stock_market})
            stock_market.thread_active = True
            thread.start()
            initialized = True
        try:
            user_in = input(":").lower()
            if user_in == "view":
                stock_market.thread_active = False
                view(stock_market, user)
                stock_market.thread_active = True
            elif user_in == "buy":
                stock_market.thread_active = False
                buy()
                stock_market.thread_active = True
            elif user_in == "sell":
                stock_market.thread_active = False
                sell()
                stock_market.thread_active = True
            elif user_in == "help":
                print("This is a stock market game. You are in the main menu.\n\
                    Your options are to view, buy, or sell stocks.\n\
                        Enter either 'view', 'buy', or 'sell'.\n\
                            or enter 'exit' to stop the game or enter\n\
                                help if you want to see this lovely message again :)")
            elif user_in == "exit":
                stock_market.thread_active = False
                break
        except KeyboardInterrupt:
            stock_market.thread_active = False
            break
    return "Thank you for playing our stock market game!"

def view(stock_market,user):
    print("Would you like to view your own stock or market stocks (enter 'my' or 'market' or 'back'):")
    user_in = input(":").lower()
    if user_in == 'my':
        user.display_user()
    elif user_in == 'market':
        for stock in stock_market.stocks:
            str(stock)
    elif user_in == "back":
        return ""
    else:
        print("invalid imput")
        view(stock_market, user)
    return ""

def buy(stock_market, user):
    print("what company's stock would you like to buy?\n\
        Your options are: 'Wonka Industries', 'Acme Corp.', 'Stark Industries',\n\
            'Wayne Enterprises', 'Soylent', 'Hooli', 'Prestige Worldwide', 'Los Pollos Hermanos',\n\
                'Oscorp', 'Iron Bank of Braavos'")
    user_in = input(":").lower()
    
    return ""

def sell():
    return ""

def timer(stocks):
    """counts time while waiting for input"""
    while stocks.thread_active:
        time.sleep(1)
        stocks.next_day()
        #print("day gone")
    return

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