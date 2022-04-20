from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import requests
import json

""" to simplify the whole process the basic assumption is market cap obtained multyplying today outstanding price for day to day adjusted close equals the daily market cap . 
Numerically the adjusted close prices of my data already reflect anysort of stock split. 
By doing like this is, i simplified a lot the process since i didn't have access to databases for historical outstanding shares or historical market caps   """

#setting some parameters and choose the car companies that will represent automotive sector market cap
companies = ["TSLA", "TYO", "BYDDF", "VWAGY", "MBG.DE", "F", "GM", "BMW.DE", "STLA", "HMC", "RACE","LCID","RIVN", "HYMTF","NIO", "LI", "VLVLY"]

stockStartDate = "2010-01-01"
today = datetime.today().strftime("%Y-%m-%d")


# manipulating data of automotive companies
df = pd.DataFrame()
shares = pd.DataFrame()

for stock in companies:
    df[stock] = web.DataReader(stock, data_source="yahoo", start=stockStartDate, end=today)["Adj Close"]

shares = web.get_quote_yahoo(companies)["sharesOutstanding"]

marketcap_bycompany = df.multiply(shares, axis=1)

marketcap_automotive = marketcap_bycompany.sum(axis=1)


# create a benchmark
apple = pd.DataFrame()
apple[stock] = web.DataReader("AAPL", data_source="yahoo", start=stockStartDate, end=today)["Adj Close"]
shares_apple = pd.DataFrame
shares_apple = web.get_quote_yahoo("AAPL")["sharesOutstanding"]
market_cap_apple = np.multiply(apple, shares_apple)


#start plotting

# create figure and axis 1
fig, ax1 = plt.subplots()

# plot line chart on axis #1
ax1.plot(marketcap_automotive, "r")
ax1.set_ylabel('automotive sector')
ax1.legend(['automotive sector'], loc="upper left")

# set up the 2nd axis
ax2 = ax1.twinx()
ax2.plot(market_cap_apple, "k")
ax2.grid(False)   # turn off grid #2
ax2.set_ylabel('apple benchmark')
ax2.legend(['apple market cap'], loc="upper right")

#show dual graph
plt.show()









