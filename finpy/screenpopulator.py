import pandas as pd
from yahoo_finance import Share

price_earning_list = []
price_sales_list = []
price_EPS_list = []
url_nyse = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"

def populate(incsv, outcsv):
    df = pd.DataFrame.from_csv(incsv)
    ticker_list = df.index.tolist()

    print ticker_list
    #for ticker in ticker_list:
    #    sharename  = Share(ticker)
    #    price_earning_list.append(sharename.get_price_earnings_ratio())
    #    price_sales_list.append(sharename.get_price_sales())
    #    price_EPS_list.append(sharename.get_EPS_estimate_current_year())

    #df = df.transpose()
    dicter = df.to_dict()
    df.to_csv(outcsv)

if __name__ == "__main__":
    populate("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download", "fixedoutput.csv")
