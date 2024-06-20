#!/usr/bin/env python3

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from config import stocks, end_date, start_date_x_days_before
from graph import draw_graph
from intersection import display_intersection

if __name__ == "__main__":
    # Create a subplot for each stock
    fig, axs = plt.subplots(len(stocks))

    for i, stock in enumerate(stocks):
        # Grab the stock data
        stock_data = yf.download(stock, start=start_date_x_days_before, end=end_date)

        # Create a DataFrame to store the intersection dates
        intersection_dates = pd.DataFrame(columns=["Date", "Type"])

        # Draw the graph
        draw_graph(stock_data, stock, axs[i])

        # Display the intersections
        intersection_dates = display_intersection(stock_data, stock, intersection_dates)

    # Show all the graphs in the same window
    plt.show()