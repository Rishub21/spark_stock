from googlefinance import getQuotes

import urllib2
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

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







#for tr in var.find_all("tr")[2:]: # skips the first row
    #print tr
