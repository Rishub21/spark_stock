"""
from django.conf import settings
settings.configure()
import models
"""
#from django.conf import settings
#settings.configure()

#import backtester
#settings.configure(default_settings=backtester, DEBUG=True)

from finpy.models import Stock
from googlefinance import getQuotes
import urllib2
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import re
from collections import defaultdict
from googlefinance import getQuotes
import datetime
from django.utils import timezone
#from datetime import timezone


print "test"

# what you want to make sure is that the sector list is passed as a string, then we will use split to convert it to a proper list
#sector_list, ratio_list, price_range, marketcap should be the different types of args available in *args

def soup(ticker):
    vardict= defaultdict(int)
    url = "https://finance.yahoo.com/quote/" + ticker + "/key-statistics?p=" + ticker
    content = urllib2.urlopen(url).read()
    only_span = SoupStrainer(["span", "td"])
    data = BeautifulSoup(content, "lxml", parse_only= only_span) # this is creating a BeautifulSoup object that we can enact BeautifulSoup methods on



    #print data.get_text()
    #find_string = data.get_text().find_all(text=re.compile('Trailing P/E'), limit=1)
    var = data.find(text = "Trailing P/E").findNext("td")
    print "SUCCESS"
    var2 = data.find(text = "Price/Book").findNext("td")
    print "SUCCESS"

    var3 = data.find(text = "PEG Ratio (5 yr expected)").findNext("td")
    print "SUCCESS"


    var4 = data.find(text = "Diluted EPS").findNext("td")
    print "SUCCESS"


    var5 = data.find(text = "Current Ratio").findNext("td")
    print "SUCCESS"

    var6 = data.find(text = "Profit Margin").findNext("td")
    print "SUCCESS"

    var7 = data.find(text = "Total Debt/Equity").findNext("td")
    print "SUCCESS"

    var8 = data.find(text = "Return on Assets").findNext("td")
    print "SUCCESS"

    var9 = data.find(text = "Operating Cash Flow").findNext("td")
    print "SUCCESS"



    var10 = data.find(text = "Beta").findNext("td")
    print "SUCCESS"

    var11 = data.find(text = "Quarterly Revenue Growth").findNext("td")
    print "SUCCESS"



    print var.text + "Soup"
    print var2.text + "Soup"
    print var3.text + "Soup"

    print var4.text + "Soup"
    print var5.text + "Soup"
    print var6.text + "Soup"
    print var7.text + "Soup"
    print var8.text + "Soup"
    print var9.text + "Soup"
    print var10.text + "Soup"
    print var11.text + "Soup"



    vardict["Price_Earnings"] = var.text
    vardict["Price_Book"] = var2.text
    vardict["Price_Earnings_Growth"] = var3.text
    #vardict["Diluted_EPS"] = var4.text


    return vardict



def screenerfunction(kwargs):

    stocks = Stock.objects.all()

    screened_sector_list = []
    screened_cap_list = []
    screened_price_list = []
    screened_ratio_list = []
    joint_list = []
    final_ratio_list = [] # this will actually get passed to final part of function not the screened_ratio_list




    full_list = [screened_sector_list, screened_cap_list, screened_price_list]
    new_full_list = []

    current_time = timezone.now()

###### ratios are going to have to be passed in dict format

    sector_list = kwargs["sector_list"]
    marketcap = kwargs["marketcap"]
    price_range = kwargs["price_range"]
    ratio_dict = kwargs["ratio_dict"]




    if sector_list is not None:
        for stock in stocks:
            for sector in sector_list:
                if stock.sector == str(sector):
                    screened_sector_list.append(stock)
        print ")))))))))))))))00"
        print screened_sector_list


    """

        # ratio_dict would have to be created in views such that there are no blanks can only be the ratios that the user inputs
        #ratio_list = soup(stock.ticker) # using BeautifulSoup to scrape the ratio values from yahoo finance
        #if ratio_dict is not None:
        #    for ratiokey in ratio_dict:
        #        if ratio_dict[ratiokey] == vardict[ratiokey]:
        #            screened_list.append(stock)
        #        else:
        #            if stock in screened_list:
        #                screened_list = screened_list.remove(stock)

    if marketcap is not None:

        if (len(sector_list) > 0 ):
            for stock in screened_sector_list:
                if stock.market_cap is not None:
                    floater = float(stock.market_cap)
                    print type(floater)

                    if(float(stock.market_cap) < 200.00 and stock.market_cap > 10.00):
                        stockcap = "Large"
                    elif(float(stock.market_cap)< 10.00 and stock.market_cap > 2.00):
                        stockcap = "Mid"
                    elif(float(stock.market_cap) < 2.00):
                        stockcap = "Small"
                    elif (float(stock.market_cap) > 200.00):
                        stockcap = "Mega"
                    for size in marketcap:
                        if(stockcap == size):
                            screened_cap_list.append(stock)


        else: # if there is no sector specified
            for stock in stocks:
                if stock.market_cap is not None:
                    if(float(stock.market_cap) < 200.00 and stock.market_cap > 10.00):
                        stockcap = "Large"
                    elif(float(stock.market_cap)< 10.00 and stock.market_cap > 2.00):
                        stockcap = "Mid"
                    elif(float(stock.market_cap) < 2.00):
                        stockcap = "Small"
                    elif (float(stock.market_cap) > 200.00):
                        stockcap = "Mega"


                    for size in marketcap:
                        if(stockcap == size):
                            screened_cap_list.append(stock)
        print "^^^^^^^^^^^^^^^^^^^^^^^"
        print screened_cap_list
        print marketcap



    if price_range is not None: # price filter
        print "Not none"
        lower_limit = float(price_range[0])
        upper_limit = float(price_range[1])
        print screened_sector_list
        print screened_cap_list
        if(len(screened_sector_list) > 0 and len(screened_cap_list) > 0):
            joint_list = list(set(screened_sector_list) and set(screened_cap_list))
            print joint_list
            print "FIRST OPTION FOR PRICE"

            if(len(joint_list) == 0 ):
                joint_list = None
                return joint_list
                # end of script, there are no matches
            else:
                for stock in joint_list:
                    time_delta = current_time - stock.last_price_refresh

                    if(time_delta.total_seconds()  < 604800) :  # of seconds in a week
                        if(float(stock.last_price) <= upper_limit and float(stock.last_price) >= lower_limit) :
                            screened_price_list.append(stock)
                    else:
                        ticker  = stock.ticker
                        current_price = getQuotes(str(ticker))
                        print current_price
                        print "THIS IS THE TICKER TO ANALYZE " + str(stock.ticker)
                        print "Making this api call to get the modern price"
                        current_price = float(current_price[0]["LastTradePrice"])

                        stock.last_price_refresh = datetime.datetime.now()
                        stock.last_price = current_price
                        stock.save()
                        # updating the stocks price since it hasnt been refreshed for a whole week
                        if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                            screened_price_list.append(stock)

        elif(len(screened_sector_list) > 0 and len(screened_cap_list) == 0) : # there is only a sector attribute, 2nd option
            for stock in screened_sector_list:
                time_delta = current_time - stock.last_price_refresh

                if(time_delta.total_seconds()  < 604,800) :  # of seconds in a week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)
                else:
                    ticker  = stock.ticker
                    current_price = getQuotes(str(ticker))
                    current_price = float(current_price[0]["LastTradePrice"])
                    stock.last_price_refresh = datetime.datetime.now()
                    stock.last_price = current_price
                    stock.save()
                    # updating the stocks price since it hasnt been refreshed for a whole week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)

        elif(len(screened_cap_list) > 0 and len(screened_sector_list) == 0 ): # there is only market_cap
            for stock in screened_cap_list:
                time_delta = current_time - stock.last_price_refresh

                if(time_delta.total_seconds()  < 604,800) :  # of seconds in a week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)
                else:
                    ticker  = stock.ticker
                    current_price = getQuotes(str(ticker))
                    current_price = float(current_price[0]["LastTradePrice"])
                    stock.last_price_refresh = datetime.datetime.now()
                    stock.last_price = current_price
                    stock.save()
                    # updating the stocks price since it hasnt been refreshed for a whole week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)
        else: # there are no sector or market cap attributes
            for stock in stocks:
                time_delta = current_time - stock.last_price_refresh

                if(time_delta.total_seconds()  < 604,800) :  # of seconds in a week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)
                else:
                    ticker  = stock.ticker
                    current_price = getQuotes(str(ticker))
                    current_price = float(current_price[0]["LastTradePrice"])
                    stock.last_price_refresh = datetime.datetime.now()
                    stock.last_price = current_price
                    stock.save()
                    # updating the stocks price since it hasnt been refreshed for a whole week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)
        print "(((((((((())))))))))"
        print(screened_price_list)


    for lister in full_list:
        if len(lister) > 0 :
            new_full_list.append(lister)  # this is a list of all the list that have been filled with arguments by the user
    print "*************"
    print full_list
    finalresult = set(new_full_list[0]) # in the following two lines we are checking to see the common elements between the first sublist and every sublist there after
    if len(new_full_list) > 1:
        for lister in new_full_list[1:]:
            finalresult.intersection_update(lister)   #  this is a list that has the stocks common to all the lists populated by the user

    print "********* INTERMEDIATE FINAL RESULT ************"
    print finalresult

    if ratio_dict is not None:

        if(len(finalresult) > 0 ) :
            pe_list =  []
            peg_list = []
            pbook_list = []
            eps_list = []
            allratio_list = [pe_list, peg_list, pbook_list, eps_list]

            for stock in finalresult:
                ratio_continue = True
                time_ratio_delta = current_time - stock.last_ratio_refresh
                #print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&777"
                #print time_ratio_delta
                if (time_ratio_delta.total_seconds() >  604800) :

                    print "MAKING THIS SOUP CALL" + str(stock.name)

                    updated_ratio_dict = soup(stock.ticker)

                    print "********* SOUP DICT ************"
                    print updated_ratio_dict
                    print updated_ratio_dict["Price_Earnings"]
                    #print updated_ratio_dict["PE_Ratio"]
                    #stocker = Stock.objects.get(ticker = stock.ticker)
                    stock.PBook_ratio = float(str(updated_ratio_dict["Price_Book"]))
                    stock.PEG_ratio = float(str(updated_ratio_dict["Price_Earnings_Growth"]))
                    stock.EPS_ratio = float(str(updated_ratio_dict["Diluted_EPS"]))
                    stock.PE_ratio = float(str(updated_ratio_dict["Price_Earnings"]))
                    stock.last_ratio_refresh = datetime.datetime.now()
                    stock.save()



                for ratio in ratio_dict:

                    if ratio == "PE_ratio" :
                        if stock.PE_ratio is not None:
                            print str(float(stock.PE_ratio) - ratio_dict["PE_ratio"])
                            if(abs(float(stock.PE_ratio) - ratio_dict["PE_ratio"]) < 2 ) :
                                print "PE SUCCESS"
                                pe_list.append(stock)
                            else:
                                continue
                        else:
                            continue


                    if ratio == "PEG_ratio":
                        print "PEG"
                        if stock.PEG_ratio is not None:
                            if (abs(stock.PEG_ratio - ratio_dict["PEG_ratio"]) < 2 ):
                                peg_list.append(stock)
                                print "PEG SUCCESS"
                            else:
                                continue
                        else:
                            continue

                    if ratio == "Price_Book":
                        if stock.PBook_ratio is not None:
                            if (abs(stock.PBook_ratio - ratio_dict["Price_Book"]) < 2 ):
                                pbook_list.append(stock)
                            else:
                                continue
                        else:
                            continue

                    if ratio == "EPS_ratio":
                        if stock.EPS_ratio is not None:
                            if (abs(stock.EPS_ratio - ratio_dict["EPS_ratio"]) < 2 ):
                                eps_list.append(stock)
                            else:
                                continue
                        else:
                                    continue
            realratio_list = []
            ratioresult = []
            for ratiolist in allratio_list:
                if len(ratiolist) > 0 :
                    realratio_list.append(ratiolist)
            ratioresult = set(realratio_list[0])
            if len(realratio_list) > 1:
                for r in realratio_list[1:]:
                    ratioresult.intersection_update(r)
            ratioresult = list(ratioresult)
            print "$$$$$$$$$$$$$$"
            print ratioresult


        else: # there was no other parameter
            pe_list =  []
            peg_list = []
            pbook_list = []
            eps_list = []
            allratio_list = [pe_list, peg_list, pbook_list, eps_list]

            for stock in finalresult:
                ratio_continue = True
                time_ratio_delta = current_time - stock.last_ratio_refresh
                #print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&777"
                #print time_ratio_delta
                if (time_ratio_delta.total_seconds() >  604800) :

                    print "MAKING THIS SOUP CALL" + str(stock.name)

                    updated_ratio_dict = soup(stock.ticker)

                    print "********* SOUP DICT ************"
                    print updated_ratio_dict
                    print updated_ratio_dict["Price_Earnings"]
                    #print updated_ratio_dict["PE_Ratio"]
                    #stocker = Stock.objects.get(ticker = stock.ticker)
                    stock.PBook_ratio = float(str(updated_ratio_dict["Price_Book"]))
                    stock.PEG_ratio = float(str(updated_ratio_dict["Price_Earnings_Growth"]))
                    stock.EPS_ratio = float(str(updated_ratio_dict["Diluted_EPS"]))
                    stock.PE_ratio = float(str(updated_ratio_dict["Price_Earnings"]))
                    stock.last_ratio_refresh = datetime.datetime.now()
                    stock.save()



                for ratio in ratio_dict:

                    if ratio == "PE_ratio" :
                        if stock.PE_ratio is not None:
                            print str(float(stock.PE_ratio) - ratio_dict["PE_ratio"])
                            if(abs(float(stock.PE_ratio) - ratio_dict["PE_ratio"]) < 2 ) :
                                print "PE SUCCESS"
                                pe_list.append(stock)
                            else:
                                continue
                        else:
                            continue


                    if ratio == "PEG_ratio":
                        print "PEG"
                        if stock.PEG_ratio is not None:
                            if (abs(stock.PEG_ratio - ratio_dict["PEG_ratio"]) < 2 ):
                                peg_list.append(stock)
                                print "PEG SUCCESS"
                            else:
                                continue
                        else:
                            continue

                    if ratio == "Price_Book":
                        if stock.PBook_ratio is not None:
                            if (abs(stock.PBook_ratio - ratio_dict["Price_Book"]) < 2 ):
                                pbook_list.append(stock)
                            else:
                                continue
                        else:
                            continue

                    if ratio == "EPS_ratio":
                        if stock.EPS_ratio is not None:
                            if (abs(stock.EPS_ratio - ratio_dict["EPS_ratio"]) < 2 ):
                                eps_list.append(stock)
                            else:
                                continue
                        else:
                                    continue
            realratio_list = []
            ratioresult = []
            for ratiolist in allratio_list:
                if len(ratiolist) > 0 :
                    realratio_list.append(ratiolist)
            ratioresult = set(realratio_list[0])
            if len(realratio_list) > 1:
                for r in realratio_list[1:]:
                    ratioresult.intersection_update(r)
            ratioresult = list(ratioresult)
            print "$$$$$$$$$$$$$$"
            print ratioresult

    full_list = [screened_sector_list, screened_cap_list, screened_price_list, ratioresult]
    #print full_list

    new_full_list = []
    for lister in full_list:
        if len(lister) > 0 :
            new_full_list.append(lister)
    #print new_full_list

    finalresult = set(new_full_list[0])
    print "FINAL RESULTS"
    print finalresult

    if len(new_full_list) > 0:
        for listing in new_full_list[1:]:
            finalresult.intersection_update(listing)

    print  "**********************FINISHED********************"

    print (finalresult)
    print len(finalresult)
    if len(finalresult) ==0 :
        print "no stocks matched"
        return 0

    return list(finalresult)

    """


if __name__ == "__main__":
    list = ["AAPL", "GOOG", "MSFT", "TSLA","FB", "TWTR", "GS"]

    for item in list:
        soup(item)
    print "FINISHED"
