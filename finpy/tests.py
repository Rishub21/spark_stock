
from googlefinance import getQuotes
import urllib2
from bs4 import BeautifulSoup
import re
from collections import defaultdict
from googlefinance import getQuotes

print "test"

# what you want to make sure is that the sector list is passed as a string, then we will use split to convert it to a proper list
#sector_list, ratio_list, price_range, marketcap should be the different types of args available in *args

def soup(ticker):
    vardict= defaultdict(int)
    url = "https://finance.yahoo.com/quote/" + ticker + "/key-statistics?p=" + ticker
    content = urllib2.urlopen(url).read()
    data = BeautifulSoup(content) # this is creating a BeautifulSoup object that we can enact BeautifulSoup methods on
    #print data.get_text()
    #find_string = data.get_text().find_all(text=re.compile('Trailing P/E'), limit=1)
    var = data.find(text = "Trailing P/E").findNext("td")
    var2 = data.find(text = "Price/Book").findNext("td")

    print var.text
    print var2.text

    vardict["PE-Ratio"] = var
    vardict["Price-Book"] = var2

    return vardict


def screenerfunction(**kwargs):

    screened_list = []

    for key in kwargs:
        if key == "sector_list":
            sector_list = kwargs[key]
        else:
            sector_list = None
        if key == "ratio_dict":
            ratio_dict = kwargs[key]
        else:
            ratio_dict = None
        if key == "marketcap":
            marketcap = kwargs[key]
        else:
            marketcap = None
        if key == "price_range":
            price_range == kwargs[key]
        else:
            sector_list = None
            # price range will probably be a tuple value

    for stock in stocks:
        if sector_list is not None:
            for sector in sector_list:
                if stock.sector == sector:
                    screened_list.append(stock)
        # ratio_dict would have to be created in views such that there are no blanks can only be the ratios that the user inputs
        ratio_list = soup(stock.ticker) # using BeautifulSoup to scrape the ratio values from yahoo finance
        if ratio_dict is not None:
            for ratiokey in ratio_dict:
                if ratio_dict[ratiokey] == vardict[ratiokey]:
                    screened_list.append(stock)
                else:
                    if stock in screened_list:
                        screened_list = screened_list.remove(stock)

        if marketcap is not None:
            # you are going to have make ranges so
            if "M" in stock.marketcap:
                stockcap = "small"
            if "B" in stock.marketcap:
                stock.marketcap.strip("B")
                stock.marketcap.strip("$")
                stockvalue = int(stock.marketcap)

                if stockvalue >= 200 :
                    stockcap = "mega"
                if stockvalue >= 10 and < 200:
                    stockcap = "large"
                if stockvalue >=2 and <10:
                    stockcap = "mid"
            if stockcap == marketcap:
                screened_list.append(stock)

            else:
                if stock in screened_list:
                    screened_list = screened_list.remove(stock)
        if price_range is not None:
            lower_limit = price_range[0]
            upper_limit = price_range[1]
            # where price range is a tuple passed from views

            current_price = getQuotes(stock.ticker)
            current_price = current_price[0]["LastTradePrice"]

            if price_range >= lower_limit and <= upper_limit:
                screened_list.append(stock)


    return screened_list
