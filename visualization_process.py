import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd


# This function visualizes the data
def visualize(data):
    fig, ax = plt.subplots(figsize=(12, 6))

    data['Date'] = pd.to_datetime(data['Date'])

    ohlc = data[['Date', 'Open', 'High', 'Low', 'Close']]

    ohlc.loc[:, 'Date'] = ohlc['Date'].apply(mdates.date2num)
    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='g', colordown='r')

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('Candlestick Chart')

    plt.xticks(rotation=45)
    plt.grid()
    plt.show()
    return print("Graph was shown")
