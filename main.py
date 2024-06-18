#!/usr/bin/env python3

import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from config import stocks, start_date, end_date, num_periods_short, num_periods_long, get_date_x_days_before
from graph import draw_graph
from intersection import display_intersection

if __name__ == "__main__":
    # Get a few days before the start date to accommodate the period size
    start_date_x_days_before = get_date_x_days_before(start_date, num_periods_long*2)

    # Create a subplot for each stock
    fig, axs = plt.subplots(len(stocks))

    for i, stock in enumerate(stocks):
        # Grab the stock data
        stock_data = yf.download(stock, start=start_date_x_days_before, end=end_date)

        # Draw the graph
        draw_graph(stock_data, stock, axs[i])

        # Display the intersections
        # display_intersection(stock_data, stock)

    # Show all the graphs in the same window
    plt.show()