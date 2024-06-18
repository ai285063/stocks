#!/usr/bin/env python3

import yfinance as yf
import datetime as dt
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

def get_date_x_days_before(date_string, num_days_before):
    date_object = dt.datetime.strptime(date_string, "%Y-%m-%d")
    new_date = date_object - dt.timedelta(days=num_days_before)
    new_date_string = new_date.strftime("%Y-%m-%d")
    return new_date_string

# Define the stock symbols and the time range for the data
# TODO: modify this if want to add more stocks
stocks = ["AAPL", "NVDA", "GOOGL", "SPY", "QQQ"]


# Define the time range for the data
# TODO: modify date if needed
end_date = datetime.now().strftime('%Y-%m-%d')  # Today's date
start_date = (datetime.now() - timedelta(days=1825)).strftime('%Y-%m-%d')  # Date 5 year ago

# TODO: modify sma periods if needed
num_periods_short = 50
num_periods_long = 150

# Get a few days before the start date to accommodate the period size
start_date_x_days_before = get_date_x_days_before(start_date, num_periods_long*2)

if __name__ == "__main__":
    # Create a figure with subplots for each stock
    fig, axs = plt.subplots(len(stocks), figsize=(14, 7*len(stocks)))

    for i, stock in enumerate(stocks):
        # Grab the stock data
        stock_data = yf.download(stock, start=start_date_x_days_before, end=end_date)

        # Compute the simple moving averages (SMA)
        stock_data["SMA_short"] = stock_data["Close"].rolling(window=num_periods_short).mean()
        stock_data["SMA_long"] = stock_data["Close"].rolling(window=num_periods_long).mean()

        # Calculate the slopes of the SMAs
        slope_short = np.polyfit(range(num_periods_short), stock_data["SMA_short"].dropna()[-num_periods_short:], 1)[0]
        slope_long = np.polyfit(range(num_periods_long), stock_data["SMA_long"].dropna()[-num_periods_long:], 1)[0]

        # Now that we calculated the SMA, we can remove the dates before the actual start date that we want.
        stock_data = stock_data[start_date:]

        # Plot the closing price and the SMAs
        axs[i].plot(stock_data["Close"], label="Close")
        axs[i].plot(stock_data["SMA_short"], color='green', label=f"{num_periods_short}-Day SMA")
        axs[i].plot(stock_data["SMA_long"], color='red', label=f"{num_periods_long}-Day SMA")
        axs[i].set_title(f"{stock} Close Prices, {num_periods_short}-Day SMA & {num_periods_long}-Day SMA")
        axs[i].set_xlabel("Date")
        axs[i].set_ylabel("Price")
        axs[i].legend()
        axs[i].grid(True)

        # Convert the start and end dates to datetime objects
        start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")

        # Add the slopes to the plot title
        axs[i].set_title(f"{stock} Close Prices, {num_periods_short}-Day SMA (Slope: {slope_short:.2f}), {num_periods_long}-Day SMA (Slope: {slope_long:.2f})")

        # Set the figure size
        fig.set_size_inches(18, 9)

        # Set the plot borders
        axs[i].set_xlim([start_date_dt, end_date_dt])
        axs[i].set_ylim([stock_data["Close"].min(), stock_data["Close"].max()])

    # Display the plots
    plt.tight_layout()
    plt.show()