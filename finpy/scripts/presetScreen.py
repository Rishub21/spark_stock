from finpy.models import Stock
import cPickle as pickle
import random
import json
import urllib2
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import random
stocks = Stock.objects.all()

def mostpopular(): # coming from cnn money
    url = "http://money.cnn.com/data/hotstocks/"
    content = urllib2.urlopen(url).read()
    only_span = SoupStrainer(["span", "td", "tr", "table", "tbody", "a"])
    data = BeautifulSoup(content, "lxml",parse_only = only_span)

    table = data.find("table", {"class" : "wsod_dataTable wsod_dataTableBigAlt" })


    rows = table.find_all("tr")

    mostpop_list = []
    for row in rows[1:]:
        td = row.find("td")
        span = td.find("a")

        mostpop_list.append(span.text)
    return mostpop_list

def undervalued():
    undervalued_list = []
    for stock in stocks :
        if stock.PE_ratio <= 1.0 and stock.PBook_ratio  <= 1.2:
            undervalued_list.append(stock)

    return undervalued_list


def undervalued_growth():
    undervalued_growth_list = []
    for stock in stocks:
        if stock.PE_ratio <= 2.0 and stock.PEG_ratio <=1.0:
            undervalued_growth_list.append(stock)

    return undervalued_growth_list

def high_growth(): # not implemented yet
    high_growth_list = []
    for stock in stocks:
        if stock.revenueGrowth >= 25.0:
            high_growth_list.append(stock)

    return high_growth_list

def low_volatility():
    low_volatility_list = []
    for stock in stocks:
        if stock.beta < .25:
            low_volatility_list.append(stock)
    return low_volatility_list

    #//////////////////////////// sector specific presets


def siliconValley():
    siliconValley_list = []
    #lister = sector_dict["Technology"]
    starter_list = []

    starter_list = Stock.objects.filter(sector = "Information Technology")
    print "#####################"
    print starter_list
    mid_list = []
    for stock in starter_list:
        if stock.current_ratio > 1.1 and stock.profit_margin > 18.0: # where 18 is the sector average

            mid_list.append(stock)
    print "^^^^^^^^^^^^^^^^^"
    print mid_list
    if len(mid_list) >= 15:
        for i in range(15):
            ran = random.randint(0,14)
            siliconValley_list.append(mid_list[ran])

    else:
        for i in range(len(mid_list)):
            siliconValley_list.append(mid_list[i])

    return siliconValley_list

def manufacturing():

    manufacturing_list = []
    #lister = sector_dict["Technology"]
    starter_list = []

    starter_list = Stock.objects.filter(sector = "Industrials")
    print "#####################"
    print starter_list
    mid_list = []
    for stock in starter_list:
        if stock.return_on_assets > 5.0 and stock.profit_margin > 18.0: # where 18 is the sector average
            mid_list.append(stock)
    print "^^^^^^^^^^^^^^^^^"
    print mid_list
    if len(mid_list) >= 15:
        for i in range(15):
            ran = random.randint(0,14)
            manufacturing_list.append(mid_list[ran])
    else:
        for i in range(len(mid_list)):
            manufacturing_list.append(mid_list[i])

    return manufacturing_list

def healthCare():
    healthCare_list = []
    #lister = sector_dict["Technology"]
    starter_list = []

    starter_list = Stock.objects.filter(sector = "Health Care")
    print "#####################"
    print starter_list
    mid_list = []
    for stock in starter_list:

        try:
            free_cash_yield = (stock.cashflow / float(stock.market_cap))
            print free_cash_yield
            if stock.return_on_assets > 6.0 and free_cash_yield > .06: # where 5.5 is the sector average
                mid_list.append(stock)
        except:
            continue
    print "^^^^^^^^^^^^^^^^^"
    print mid_list
    if len(mid_list) >= 15:
        for i in range(15):
            ran = random.randint(0,14)
            healthCare_list.append(mid_list[ran])
    else:
        for i in range(len(mid_list)):
            healthCare_list.append(mid_list[i])

    return healthCare_list


def finance():
    finance_list = []
    #lister = sector_dict["Technology"]
    starter_list = []

    starter_list = Stock.objects.filter(sector = "Financials")
    print "#####################"
    print starter_list
    mid_list = []

    for stock in starter_list:
        try:
            if stock.return_on_assets >= 1.0 and stock.profit_margin > 17.0: # where 17 is the industry standard. Remeber banks are highly leveraged, meaning that they have a huge amount of debt compared to their equity. But since debt is techinically an asset, even a 1% ROA is large profits and a big deal
                mid_list.append(stock)
        except:
            continue
    print "^^^^^^^^^^^^^^^^^"
    print len(mid_list)
    if len(mid_list) >= 15:
        for i in range(15):
            ran = random.randint(0,14)
            finance_list.append(mid_list[ran])
    else:
        for i in range(len(mid_list)):
            finance_list.append(mid_list[i])

    return finance_list


def energy():
    energy_list = []
    #lister = sector_dict["Technology"]
    starter_list = []

    starter_list = Stock.objects.filter(sector = "Energy")
    print "#####################"
    mid_list = []

    for stock in starter_list:
        print "()"
        print stock.debt_equity_ratio
        print stock.profit_margin
        try:
            if stock.debt_equity_ratio < 115.0 and stock.profit_margin > 5.0: # 
                mid_list.append(stock)
        except:
            continue
    print "^^^^^^^^^^^^^^^^^"
    print len(mid_list)
    if len(mid_list) >= 15:
        for i in range(15):
            ran = random.randint(0,14)
            energy_list.append(mid_list[ran])
    else:
        for i in range(len(mid_list)):
            energy_list.append(mid_list[i])

    return energy_list
