import pandas as pd
import yfinance as yf
import webbrowser
import os
from config import stocks, start_date_x_days_before, end_date, sma_periods_short, sma_periods_long

def display_intersection(stock_data, stock, intersection_dates):
    # Calculate the SMAs
    stock_data["SMA_short"] = stock_data["Close"].rolling(window=sma_periods_short).mean()
    stock_data["SMA_long"] = stock_data["Close"].rolling(window=sma_periods_long).mean()

    # Calculate the slopes for the SMAs
    stock_data["Slope_SMA_short"] = stock_data["SMA_short"].diff()  # Slope as difference
    stock_data["Slope_SMA_long"] = stock_data["SMA_long"].diff()  # Slope as difference

    # Calculate the intersections between the short and long SMAs
    stock_data["Intersection"] = 0
    stock_data.loc[stock_data["SMA_short"] > stock_data["SMA_long"], "Intersection"] = 1
    stock_data["Intersection"] = stock_data["Intersection"].diff()

    # return intersection_dates
    for i in range(len(stock_data)):
        if stock_data["Intersection"].iloc[i] == 1 or stock_data["Intersection"].iloc[i] == -1:
            intersection_type = "Golden Cross" if stock_data["Intersection"].iloc[i] == 1 else "Death Cross"
            slope_short = stock_data["Slope_SMA_short"].iloc[i]
            slope_long = stock_data["Slope_SMA_long"].iloc[i]
            intersection_dates = pd.concat([intersection_dates, pd.DataFrame({
                "Date": [stock_data.index[i].strftime('%Y-%m-%d')],
                "Type": [intersection_type],
                f"{sma_periods_short}SMA Slope": [slope_short],
                f"{sma_periods_long}SMA Slope": [slope_long]
            })], ignore_index=True)

    return intersection_dates

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, `'color: green'` for positive strings, and
    black otherwise.
    """
    color = 'red' if val == 'Death Cross' else 'green' if val == 'Golden Cross' else 'black'
    return 'color: %s' % color

# Specify the directory path
dir_path = "htmlFiles"

# If the directory doesn't exist, create it
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Open the HTML file for writing
html_file = os.path.join(dir_path, "intersection_dates.html")
with open(html_file, 'w') as f:
    f.write('<html><body>\n')

    # Loop through each stock
    for stock in stocks:
        # Get the stock data
        stock_data = yf.download(stock, start=start_date_x_days_before, end=end_date)

        # Create a DataFrame to store the intersection dates
        intersection_dates = pd.DataFrame(columns=["Date", "Type"])

        # Calculate and display the intersections
        intersection_dates = display_intersection(stock_data, stock, intersection_dates)

        # Write the stock name and intersection dates to the HTML file
        f.write(f'<h1>{stock}</h1>\n')
        f.write(intersection_dates.style.map(color_negative_red).to_html())
        f.write('<br/>\n')

    f.write('</body></html>\n')

# Open the HTML file in the default web browser
webbrowser.open('file://' + os.path.realpath(html_file))