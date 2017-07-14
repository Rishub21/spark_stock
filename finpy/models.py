from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime



class Stock(models.Model):

    ticker = models.CharField(max_length = 10)
    name = models.CharField(max_length = 128)
    current_price = models.FloatField(default = 0.0, null = True)
    previous_price = models.FloatField(default = 0.0, null = True) # this is how we are going to calculate the price change
    market_cap = models.CharField(max_length = 20, null = True)
    sector = models.CharField(max_length = 128)
    PE_ratio = models.FloatField(default = 0.0, null = True)
    EPS_ratio = models.FloatField(default = 0.0, null = True)
    PBook_ratio = models.FloatField(default = 0.0, null = True )

    PEG_ratio = models.FloatField(default = 0.0 , null = True)  # these are the ones that we will have to make scrape calls for
    current_ratio = models.FloatField(default = 0.0 , null = True)
    profit_margin = models.FloatField(default = 0.0 , null = True)
    debt_equity_ratio = models.FloatField(default = 0.0 , null = True)
    return_on_assets  = models.FloatField(default = 0.0 , null = True)
    cashflow = models.FloatField(default = 0.0 , null = True)
    beta = models.FloatField(default = 5 , null = True)
    revenueGrowth = models.FloatField(default = 0.0 , null = True) # revenue not earnings

    last_price_refresh = models.DateTimeField(default=datetime.now) # notice we are not putting datetime.now() with paranthesis. Plan on updating this every week
    last_ratio_refresh = models.DateTimeField(default = datetime.now) # Plan on updating the ratios every month

    class Meta :
        app_label = "finpy"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.ticker

    def as_json(self):
        return dict(
            ticker = self.ticker,
            name = self.name,
            current_price = self.current_price,
            previous_price = self.previous_price,
            market_cap = self.market_cap, 

        )

class test(models.Model):
    name = models.CharField(max_length = 10 )

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    email = models.CharField(max_length = 100)
    username = models.CharField(max_length = 50)
    #bio = models.TextField(max_length=500, blank=True)
    networth = models.IntegerField(default = 15000,)
    cash = models.IntegerField(default = 15000)
    holdingsdict = JSONField(default = dict)
    history = JSONField(default = dict)
    created = models.DateTimeField(default=datetime.now) # notice we are not putting datetime.now() with paranthesis. Plan on updating this every week


    def __str__(self):
        return self.username

class savedScreener(models.Model): # these belong to a specific user profile
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(UserProfile)
    sectors = JSONField(default = dict, blank = True) # later on we are going to have to split this string into a list
    lower_limit = models.IntegerField(default = 0)
    upper_limit = models.IntegerField(default = None, blank = True)
    ratios = JSONField(default = dict, blank = True)
    last_used = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name
"""


class Screener(models.Model):
    name = models.TextField(max_length = 500, blank = True)
    date_lastused = models.
"""
# class test(models.Model):
#     name = models.CharField(max_length = 128)



    # install class Meta if you want some additional ordering of the instances
