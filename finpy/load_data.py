import sys,os
import csv
#from backtester import settings
from models import Stock
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'backtester.settings'
#settings.configure(DEBUG=True)
sys.path.append("/Users/anitanahar/Desktop/PythonProjects/Firstfinancialproject/backtester")
with open ("/Users/anitanahar/Desktop/PythonProjects/Firstfinancialproject/backtester/fixedoutput.csv", "r" ) as csv:
    next(csv) # skip first line
    for line in csv :
        liner = line.split(",")
        stock = Stock()
        stock.ticker =  liner[0]
        stock.save()
