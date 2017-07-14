import random
import cPickle as pickle
from collections import defaultdict
import urllib2
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from googlefinance import getQuotes


def soup(ticker):


    vardict= {}



    url = "https://finance.yahoo.com/quote/" + ticker + "/key-statistics?p=" + ticker
    content = urllib2.urlopen(url).read()
    only_span = SoupStrainer(["span", "td"])
    data = BeautifulSoup(content, "lxml", parse_only= only_span) # this is creating a BeautifulSoup object that we can enact BeautifulSoup methods on

    #print data.get_text()
    #find_string = data.get_text().find_all(text=re.compile('Trailing P/E'), limit=1)

    var2 = getQuotes(str(ticker))
    var2 = float(var2[0]["LastTradePrice"])
    vardict["Price"] = var2





    try:
        var12 = data.find(text = "Market Cap (intraday)").findNext("td")
        vardict["Market Cap"] = float((var12.text).strip("B"))
    except:
        vardict["Market Cap"] = None

    try:
        var3 = data.find(text = "PEG Ratio (5 yr expected)").findNext("td")
        print "SUCCESS"
        vardict["Price_Earnings_Growth"] = float((var3.text).strip("%"))
    except:
        vardict["Price_Earnings_Growth"] = None

    try :
        var4 = data.find(text = "Current Ratio").findNext("td")
        print "SUCCESS"
        vardict["Current_Ratio"] = float(var4.text)
    except:
        vardict["Current_Ratio"] = None


    try:
        var5 = data.find(text = "Profit Margin").findNext("td")
        print "SUCCESS"
        vardict["Profit_Margin"]  = float((var5.text).strip("%"))
    except:
        vardict["Profit_Margin"]  = None

    try:
        var6 = data.find(text = "Total Debt/Equity").findNext("td")
        print "SUCCESS"
        vardict["Debt_Equity"] = float(var6.text)
    except:
        vardict["Debt_Equity"] = None


    try:
        var7 = data.find(text = "Return on Assets").findNext("td")
        print "SUCCESS"
        vardict["Return_Assets"] = float((var7.text).strip("%"))
    except:
        vardict["Return_Assets"] = None

    try:
        var8 = data.find(text = "Operating Cash Flow").findNext("td")
        print "SUCCESS"
        vardict["Operating_Cash"] = float((var8.text).strip("B"))
    except:
        vardict["Operating_Cash"] = None

    try:
        var9 = data.find(text = "Beta").findNext("td")
        print "SUCCESS"
        vardict["Beta"] = float(var9.text)
    except:
        vardict["Beta"] = None

    try:
        var10 =  data.find(text = "Trailing P/E").findNext("td")
        vardict["Price_Earnings"] = float(var10.text)
    except:
        vardict["Price_Earnings"] = None
    try:
        var11 = data.find(text = "Diluted EPS").findNext("td")
        vardict["EPS"] = float(var11.text)
    except:
        vardict["EPS"] = None


    try:
        var13 = data.find(text = "Price/Book").findNext("td")
        vardict["Price_Book"] = float(var13.text)
    except:
        vardict["Price_Book"] = None
    try:
        var14 = data.find(text = "Quarterly Revenue Growth").findNext("td")
        print "SUCCESS"
        vardict["Quarterly_Growth"] = float((var14.text).strip("%"))
    except:
        vardict["Quarterly_Growth"] = None



    for key in vardict:
        if vardict[key] == "N/A":
            vardict[key] = None
    #vardict["Diluted_EPS"] = var4.text
    return vardict


master_dict = {}

with open("s&P500.csv", "r") as spfile:
    for line in spfile:
        stock_line = line.split(",")

        Ticker = stock_line[0]
        print Ticker

        stock_dict = soup(Ticker)
        master_dict[Ticker] = stock_dict

    pickle.dump(master_dict, open("master_ratios.p", "wb"))




    """
        Name  = stock_line[1]
        Sector = stock_line[2]
        Price = stock_line[3]
        Price_Earnings = stock_line[5]
        Earnings_Share = stock_line[6]
        Market_Cap = stock_line[10]
        Price_Book = stock_line[13]

        stock_dict = soup(Ticker)


        stock = Stock(ticker = Ticker, name = Name, sector = Sector, last_price = Price, PE_ratio = Price_Earnings, EPS_ratio = Earnings_Share, market_cap = Market_Cap, PBook_ratio = Price_Book, id = ID )


        stock.PEG_ratio = stock_dict["Price_Earnings_Growth"]
        stock.current_ratio = stock_dict["Current_Ratio"]
        stock.profit_margin  = stock_dict["Profit_Margin"]
        stock.debt_equity_ratio = stock_dict["Debt_Equity"]
        stock.return_on_assets = stock_dict["Return_Assets"]
        stock.cashflow = stock_dict["Operating_Cash"]
        stock.beta = stock_dict["Beta"]
        stock.revenueGrowth = stock_dict["Quarterly_Growth"]

        try:
            stock.save()
            print "SAVED"
        except:
            print "SKIPPING"
            continue
    """
