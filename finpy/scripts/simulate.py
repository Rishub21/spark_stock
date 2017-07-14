import pandas_datareader.data as web
import datetime

def newtotals(stockdict):
    for key in stockdict:
        if key == "ticker" :
            ticker = stockdict[key]
        if key == "quantitity":
            quantitity = stockdict[key]
        if key == "action":
            action = stockdict[key]
    current_date  = datetime.date.today()
    price  = web.DataReader(ticker,"yahoo", current_date, current_date)
    print price

if __name__ == "__main__":

    stockdict = {
                    "ticker" : "GOOG"
                        }
    newtotals(stockdict)
