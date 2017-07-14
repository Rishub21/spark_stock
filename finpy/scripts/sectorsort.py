import cPickle as pickle

finance_list = []  # Financials
technology_list = [] # Information Technology  or Technology
industrials_list = [] # Industrials
materials_list = [] # Materials
telecom_list = [] # Telecommunications
healthcare_list = [] # Health Care
energy_list = [] # Energy
consumer_staples_list = [] # Consumer Staples
consumer_discretionary_list = [] # Consumer Discretionary
utilities_list = [] # Utilities
real_estate_list = []

sector_dict = {}
"""
with open("s&P500.csv", "r") as spfile:
    for line in spfile:
        stock_line = line.split(",")

        if stock_line[2] == "Financials":
            finance_list.append(stock_line[0])
        elif stock_line[2] == "Technology" or stock_line[2] == "Information Technology":
            technology_list.append(stock_line[0])
        elif stock_line[2] == "Industrials":
            industrials_list.append(stock_line[0])
        elif stock_line[2] == "Materials":
            materials_list.append(stock_line[0])
        elif stock_line[2] == "Telecommunications Services":
            telecom_list.append(stock_line[0])
        elif stock_line[2] == "Health Care":
            healthcare_list.append(stock_line[0])
        elif stock_line[2] == "Energy":
            energy_list.append(stock_line[0])
        elif stock_line[2] == "Consumer Staples":
            consumer_staples_list.append(stock_line[0])
        elif stock_line[2] == "Consumer Discretionary":
            consumer_discretionary_list.append(stock_line[0])
        elif stock_line[2] == "Utilities":
            utilities_list.append(stock_line[0])
        elif stock_line[2] == "Real Estate":
            real_estate_list.append(stock_line[0])

sector_dict["Financials"] = finance_list
sector_dict["Technology"] = technology_list
sector_dict["Industrials"] = industrials_list
sector_dict["Materials"] = materials_list
sector_dict["Telecommunications"] = telecom_list
sector_dict["Health Care"] = healthcare_list
sector_dict["Energy"] = energy_list
sector_dict["Consumer Staples"] = consumer_staples_list
sector_dict["Consumer Discretionary"] = consumer_discretionary_list
sector_dict["Utilities"] = utilities_list
sector_dict["Real Estate"] = real_estate_list



pickle.dump(sector_dict, open("sectorsave.p", "wb"))

"""

sector_dict = pickle.load(open("sectorsave.p", "rb"))

print sector_dict
