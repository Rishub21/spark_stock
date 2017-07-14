import pandas_datareader.data as web
import datetime
from yahoo_finance import Share
from collections import defaultdict

holdings = defaultdict(int)

def getlimits(stock, newtotal):
    price = Share(ticker).get_price()
    max_sell = holdings[stock]
    max_buy =  int(newtotal / price) 


def newtotals(stockdict, newtotal):
    for key in stockdict:
        if key == "ticker" :
            ticker = stockdict[key]
        if key == "quantitity":
            quantitity = stockdict[key]
        if key == "action":
            action = stockdict[key]
    current_date  = datetime.date.today()
    price  = Share(ticker).get_price()
    subtotal = price * quantitity

    if action == "buy":
        subtotal = -1 * subtotal
        holdings[ticker] += quantitiy
    if action == "sell"
        holdings[ticker] -= quantitiy
    newtotal = newtotal + subtotal

    return newtotal

if __name__ == "__main__":

    stockdict = {
                    "ticker" : "GOOG"
                        }
    newtotals(stockdict)
