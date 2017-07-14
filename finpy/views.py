from django.shortcuts import render, redirect
from django.http import HttpResponse
#from portfolio_constructor import get_adjusted_close
#from finpy.screener import match_params
from collections import defaultdict
import os
import csv
from finpy.models import Stock, test, UserProfile, savedScreener
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from scripts.screener import soup, screenerfunction
from googlefinance import getQuotes
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from scripts.presetScreen import low_volatility, undervalued, mostpopular, undervalued_growth, high_growth, siliconValley, manufacturing, healthCare, finance, energy
import random
import cPickle as pickle
import json



#from scripts.simulate import newtotals

#python manage.py runserver --settings=backtester.settings
ticker_list = []
# Create your views here.

#x = lister2.delay(None, None, None)


def signup(request):
    print "RENDERING"
    if request.method == "POST":
        print "HEY THERE"
        username = request.POST.get("username")
        #email = request.POST.get("email")
        #password = request.POST.get("password")
        print username
        #print email
        #user = User.objects.create_user(username, email, password)
        #user.save()

        #prof = UserProfile(email, username)
        #prof.save()

        return redirect("landing_page")

    response  = render(request, "finpy/signup.html")
    return response






def validate_username(request):
    print "SENDING THIS AJAX CALL"
    username = request.GET.get('username', None) # where none acts as the default value of username if none is passed
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def practiceAjax(request):
    data = {
        "name" : str("AJjAX")
    }
    return JsonResponse(data)

def lowVolatility(request):
    results = []
    data = {}
    low_volatility_list = low_volatility()

    for stock in low_volatility_list:
        data[stock.name] = stock.as_json()
    #results = [stock.as_json() for stock in low_volatility_list]
    #data = {"low_volatility_list" : results}

    return JsonResponse(data)

def underValued(request):
    results = []
    data = {}
    undervalued_list = undervalued()
    print undervalued_list
    for stock in undervalued_list:
        data[stock.name] = stock.as_json()
    return JsonResponse(data)

def mostPopular(request):


    results = []
    data = {}
    mostpop_list = mostpopular()
    print mostpop_list
    for tickername in mostpop_list:
        try:
            stock = Stock.objects.get(ticker = tickername)
            data[stock.name] = stock.as_json()
        except:
            print "continue"
            continue
    return JsonResponse(data)

def undervalued_Growth(request):
    results = []
    data = {}
    undergrowth_list = undervalued_growth()
    for stock in undergrowth_list:
        data[stock.name] = stock.as_json()
    print "LENGTH" + str(len(undergrowth_list))
    return JsonResponse(data)

def highGrowth(request):
    results = []
    data = {}
    highgrowth_list= high_growth()
    print highgrowth_list
    for stock in highgrowth_list:
        data[stock.name] = stock.as_json()
    print "LENGTH" + str(len(highgrowth_list))
    return JsonResponse(data)

def silicon_Valley(request):
    results = []
    data = {}
    silicon_list = siliconValley()
    for stock in silicon_list:
        data[stock.name] = stock.as_json()
    print "LENGTH" + str(len(silicon_list))
    return JsonResponse(data)

def Manufacturing(request):
    results = []
    data = {}
    manufacturing_list = manufacturing()
    for stock in manufacturing_list:
        data[stock.name] = stock.as_json()

    print "LENGTH" + str(len(manufacturing_list))
    return JsonResponse(data)

def HealthCare(request):
    results = []
    data = {}
    healthCare_list = healthCare()
    for stock in healthCare_list:
        data[stock.name] = stock.as_json()

    print "LENGTH" + str(len(healthCare_list))
    return JsonResponse(data)

def Finance(request):
    results = []
    data = {}
    finance_list = finance()
    for stock in finance_list:
        data[stock.name] = stock.as_json()

    print "LENGTH" + str(len(finance_list))
    return JsonResponse(data)

def Energy(request):
    results = []
    data = {}
    energy_list = energy()
    for stock in energy_list:
        data[stock.name] = stock.as_json()

    return JsonResponse(data)


def chart(request):

    lister = [1,1,10]
    labels = ["10clones1","10clones2", "10clones3"]

    response = render(request, "finpy/chart.html", {"lister" : lister, "labels" : labels})
    return response

def socialogin(request):

   if request.user.is_authenticated() :
       print "AUTHENICATED"



       obj=  request.user
       print obj.email
       print obj.username

       profiles = UserProfile.objects.all()
       print profiles



       try :
           chosenOne = UserProfile.objects.get(email = obj.email)
       except:
            chosenOne = None

       print "THE CHOSEN ONE"
       print chosenOne

       if (chosenOne is None):
           newProfile = UserProfile( email = obj.email, username = obj.username, cash = 15000, networth = 15000)
           newProfile.save()
           return redirect("landing_page")


       else:
            return redirect("landing_page")


   else : # get request
        print "NOT AUTHENICATED"
        return render_to_response('finpy/social_login.html')


def loggingIn(request):

    if request.method == "POST" :
        users = User.objects.all()
        print users
        chosenName = request.POST.get("username")
        password = request.POST.get("password")
        """
        try:
            chosenOne = User.objects.get(username = chosenName)
        except:
            chosenOne = None
        """

        chosenOne = authenticate(username = chosenName, password = password)

        print "THIS IS USER"
        print chosenOne

        if chosenOne is not None:
            login(request, chosenOne)
            return redirect("landing_page")
        else:
            notValid = True
            return render_to_response("finpy/login.html", {"notValid" : notValid})
    return render_to_response('finpy/login.html')



def altLogin(request):  # gooogle signin
    return render_to_response("finpy/google_signin.html")

def loggingout(request):
    logout(request)

    return redirect("landing_page")
    ticker = models.CharField(max_length = 10)
    name = models.CharField(max_length = 128)
    last_price = models.FloatField(default = 0.0)
    market_cap = models.FloatField(default = 0.0)
    sector = models.CharField(max_length = 128)
    PE_ratio = models.FloatField(default = 0.0)
    EPS_ratio = models.FloatField(default = 0.0)
    PBook_ratio = models.FloatField(default = 0.0)
    PEG_ratio = models.FloatField(default = 0.0) # also get rid of this
    beta = models.FloatField(default = 5)
    revenueGrowth = models.FloatField(default = 0.0) # revenue not earnings
    last_price_refresh = models.DateTimeField(default=datetime.now) # notice we are not putting datetime.now() with paranthesis. Plan on updating this every week
    last_ratio_refresh = models.DateTimeField(default = datetime.now) # Plan on updating the ratios every month



def landing_page(request):
    print request.user
    print "That was the user object request for the second time "

    #stock = Stock(ticker = "YH",name = "Yahoo", last_price =  130.0, market_cap = "200", sector = "Technology",PE_ratio =  15.0, EPS_ratio =  12.0, PBook_ratio =  10.0, PEG_ratio = 11.0, beta = 3.0, revenueGrowth =  22.5, id = 1234556)
    #stock.save()

    # to update the stocks,


    stock_dict = pickle.load(open("/Users/rishubnahar/Desktop/djangoprojects/paper-trader/backend/backtester/finpy/master_ratios.p", "rb"))
    print stock_dict["MSFT"]

    with open("/Users/rishubnahar/Desktop/djangoprojects/paper-trader/backend/backtester/finpy/s&P500.csv", "r") as spfile:
        for line in spfile:
            stock_line = line.split(",")
            ID = random.randint(100000,999999)

            Ticker = stock_line[0]
            Name  = stock_line[1]
            Sector = stock_line[2]
            stock = Stock.objects.get(name = Name)
            stock.previous_price = stock.current_price
            stock.current_price = stock_dict[Ticker]["Price"]
            stock.PE_ratio  = stock_dict[Ticker]["Price_Earnings"]
            stock.EPS_ratio = stock_dict[Ticker]["EPS"]
            stock.market_cap = stock_dict[Ticker]["Market Cap"]
            stock.PBook_ratio = stock_dict[Ticker]["Price_Book"]
            #stock = Stock(ticker = Ticker, name = Name, sector = Sector, last_price = Price, PE_ratio = Price_Earnings, EPS_ratio = Earnings_Share, market_cap = Market_Cap, PBook_ratio = Price_Book, id = ID )
            try:
                stock.PEG_ratio = stock_dict[Ticker]["Price_Earnings_Growth"]
            except:
                stock.PEG_ratio = None
            try :
                stock.current_ratio = stock_dict[Ticker]["Current_Ratio"]
            except :
                stock.current_ratio = None
            try:
                stock.profit_margin = stock_dict[Ticker]["Profit_Margin"]
            except:
                stock.profit_margin = None
            try:
                stock.debt_equity_ratio = stock_dict[Ticker]["Debt_Equity"]
            except:
                stock.debt_equity_ratio = None
            try:
                stock.return_on_assets = stock_dict[Ticker]["Return_Assets"]
            except :
                stock.return_on_assets = None
            try:
                stock.cashflow = stock_dict[Ticker]["Operating_Cash"]
            except:
                stock.cashflow = None
            try:
                stock.beta = stock_dict[Ticker]["Beta"]
            except:
                stock.beta = None
            try:
                stock.revenueGrowth = stock_dict[Ticker]["Quarterly_Growth"]
            except:
                stock.revenueGrowth = None

            stock.save()
            print "stocking up"


    if (request.user.is_authenticated()):
        print "UUSER"
        print request.user.username
        response = render(request,"finpy/landing_page.html", {"user" : request.user})
    response = render(request,"finpy/landing_page.html")
    return response
    #stock = Stock.objects.all()

    print "************TASK STATE*************"
    #x = lister2.delay()
    #print x.request
    """
    #celery_task_result = AsyncResult(x.task_id)
    task_state = celery_task_result.state
    print task_state
    #print x.task_id
    #print str(lister2.AsyncResult(x.task_id).state)


    """


    if request.method == "POST":
        stockquery = request.POST.get("stockquery")
        global ticker_list
        tickerlist.append(stockquery)



def plotter(request):

    if request.method == "POST":
        startDate = request.POST.get("starting")
        endDate = request.POST.get("end")
        get_adjusted_close(ticker_list, startDate, endDate)

def screener(request) :
        name = request.GET.get('name') # where none acts as the default value of username if none is passed
        print "THIS IS the DATA"
        print name
        sectors = request.GET.get("sectors").split(",")


        sectors = request.GET.get("sectors").split(",")
        ratios = json.dumps(request.GET.get("ratios")) # this is a json object
        prices = request.GET.get("prices").split(",")
        marketcap = request.GET.get("marketcap").split(",")
        data = {
                 "sector_list" : sectors,
                 "price_range" : prices,
                 "ratio_dict" :ratios,
                 "market_cap" : marketcap,

        }

        print data


        screenerfunction(data)

        return HttpResponse(data)




        """
        ticker_list = []
        target_list = []

        # set every attribute to none as default

        passed_dict = {}

        if request.method == "POST":

            #lister2.delay()
            #x = lister2.delay()

            print "************REQUESt***********"
        #    print x.task_id
        #    print x.backend

        #    print str(lister2.AsyncResult(x.task_id).state)


            #for i in range(100000000):
                #print i
            sector_name = []
            final_sector = []

            print "testing this POST"
            sector_name.append(request.POST.get("Technology"))
            sector_name.append(request.POST.get("Health Care"))
            sector_name.append(request.POST.get("Finance"))
            sector_name.append(request.POST.get("Consumer Services"))
            sector_name.append(request.POST.get("Consumer Durables"))
            print "TRY"
            print sector_name
            #market_cap = request.POST.get("market_cap")
            #print "THIS IS MARKET CAP" + str(market_cap)
            for sector in sector_name:
                if sector is not  None:
                    final_sector.append(sector)


            passed_dict["sector_list"] = final_sector
            print "TRY@xwxs"
            print final_sector
            #passed_dict["marketcap"] = market_cap
            #target_list =  match_params("shortoutput.csv", passed_dict)
            screenerfunction(passed_dict)

            response  = render(request, "finpy/Frontend/html/screener.html", {"target_list" : target_list })
            return response

        response  = render(request, "finpy/Frontend/html/screener.html")
        return response
        """

def screenerDash(request):
    print "screeneruser"
    print request.user.username


    saved_screeners = savedScreener.objects.all()
    passed_screeners = {}
    passed_bul = True

    for screener in saved_screeners:
        print screener
        passed_screeners[screener] = ["default"]
        if str(screener.user) == str(request.user.username):
            for sector in screener.sectors:
                print "THIS is sector"
                print screener.sectors[sector]
                for part in screener.sectors[sector]:
                    print "This is part"
                    print part
                    passed_screeners[screener].append(str(part))
    print passed_screeners
    if len(passed_screeners) > 0 : # if there is at least one screener that matches who ever the user happens to be at the time
        passed_bul = False

    practicedict = {"a" : [1,2,3], "b" : [3,4,5]}
    print "*((((**))))"
    print passed_screeners
    print practicedict

    response =  render(request,"finpy/front-end/HTML/screener-saved.html", {"passed_screeners" : passed_screeners, "passed_bul" : passed_bul, "practicedict" : practicedict})
    return response

def screenerCreate(request):
    response = render(request, "finpy/front-end/HTML/screener-create.html")
    return response




def screener2(request) :

    if request.method == "POST":
        sector = request.POST["sector"]

    target_list = []
    passed_dict = defaultdict(list)
    passed_dict["Sector"] == sector

    target_list =  match_params("shortoutput.csv", passed_dict)
    return HttpResponse("SUCCESS!")


def pdfDownload(request):
    path = ("finpy/s&P500.csv")
    filename = open(path, "r")
    response = HttpResponse(filename, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="s&P500.csv"'

    return response







if __name__ == "__main__":
    print "HI"
