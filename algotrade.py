from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.technical import ma

feed = yahoofeed.Feed()

print feed

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        super(MyStrategy, self).__init__(feed,1000)
        self.__position = None
        self.__instrument = instrument # which stock we talking about
        self.setUseAdjustedValues(True)
        self.__sma = ma.SMA(feed[instrument].getPriceDataSeries(), smaPeriod)

    def onEnterOk(self, position):
        # so execInfo i sgetting all the information of the last trade with the first command
        execInfo = position.getEntryOrder().getExecutionInfo
        # then we get the exact price of the last trade of this stock with this next command
        self.info("BUY at $%.2f" % (execInfo.getPrice))

    def onEnterCanceled(self, position):
        self.__position = None

    def onExitOk(self, position) :
        execInfo = position.getExitOrder().getExecutionInfo
    def onExitCanceled(self, position):
        self.__position.exitMarket()

    def onBars(self, bars):
         
