from Stock import Stock
from StockMarket import StockMarket
import time
import threading

def main():
    #valid commands 
    running = True
    initialized = False
    stock_market = StockMarket()
    while running:
        if not initialized:
            cash = startup()
            #thread = threading.Thread(target = time, args = [stock_market])
            #thread.start()
            initialized = True
        user_in = input(":")
        user_in = user_in.lower()
        if user_in == "view":
            view()
        elif user_in == "buy":
            buy()
        elif user_in == "sell":
            sell()
        elif user_in == "exit":
            break
    return "Thank you for playing our stock market game!"

def view():
    return ""

def buy():
    return ""

def sell():
    return ""

def timer(args):
    """counts time while waiting for input"""
    while True:
        time.sleep(1)
        args[0].next_day()
        print("day gone")
    return

def startup():
    #initialize the stock market game
    #will return with initial money count and user name
    print("Hello, welcome to the stock market game!\n\
This game consists of buying and selling stock with\n\
the purpose of simulating the real stock market.\n\n\
In this game the stocks are reflections of the real\n\
stock market however, there are fictionalized busts\n\
and booms. So try not to lose everything or if you do,\n\
just restart :)      Good Luck!\n")
    while True:
        init_money = input("Please enter starting cash amount(1-10,000): ")
        if init_money.isdigit() and 0 < len(init_money) < 5:
            break
        else:
            print("Invalid amount")
    return init_money

if __name__ == "__main__":
    print(main())