import matplotlib.pyplot as plt
from matplotlib.dates import num2date
import mplcursors
import pandas as pd
from config import sma_periods_short, sma_periods_long

def draw_graph(stock_data, stock, ax):
    # Calculate the SMAs
    stock_data["SMA_short"] = stock_data["Close"].rolling(window=sma_periods_short).mean()
    stock_data["SMA_long"] = stock_data["Close"].rolling(window=sma_periods_long).mean()

    # # Draw the closing prices
    ax.plot(stock_data["Close"], label="Close")

    # Calculate the slopes of the SMAs
    slope_short_series = stock_data["SMA_short"].diff()  # Slope as difference
    slope_long_series = stock_data["SMA_long"].diff()  # Slope as difference

    # Use the last value of the slope series for labeling
    slope_short_last_value = slope_short_series.iloc[-1]
    slope_long_last_value = slope_long_series.iloc[-1]

    # Draw the SMAs with corrected labels
    ax.plot(stock_data["SMA_short"], color='green', label=f"{sma_periods_short}-Day SMA (Slope: {slope_short_last_value:.2f})")
    ax.plot(stock_data["SMA_long"], color='red', label=f"{sma_periods_long}-Day SMA (Slope: {slope_long_last_value:.2f})")

    # Set the title and labels
    ax.set_title(f"{stock} Close Prices, {sma_periods_short}-Day SMA & {sma_periods_long}-Day SMA")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")

    # Set the plot borders
    ax.set_xlim([stock_data.index.min(), stock_data.index.max()])
    ax.set_ylim([stock_data["Close"].min(), stock_data["Close"].max()])

    # Show the legend
    ax.legend()

    # Enable the grid
    ax.grid(True)

    # Set the figure size
    fig = plt.gcf()
    fig.set_size_inches(18, 9)

    # Enable the hover feature and modify hover label
    cursor = mplcursors.cursor(ax, hover=True)
    @cursor.connect("add")
    def on_add(sel):
        x, y = sel.target
        x_date = num2date(x).date()  # Convert x from a number to a date
        x_datetime = pd.to_datetime(x_date)  # Convert to pandas datetime

        # Find the nearest index using searchsorted
        insert_loc = stock_data.index.searchsorted(x_datetime)

        # Handle edge cases
        if insert_loc == len(stock_data.index):
            hovered_index = insert_loc - 1  # Use the last index if out of bounds
        elif insert_loc == 0:
            hovered_index = 0  # Use the first index if x_datetime is before all dates
        else:
            left_diff = x_datetime - stock_data.index[insert_loc - 1]
            right_diff = stock_data.index[insert_loc] - x_datetime
            hovered_index = insert_loc - 1 if left_diff < right_diff else insert_loc

        slope_short_at_hover = slope_short_series.iloc[hovered_index]
        slope_long_at_hover = slope_long_series.iloc[hovered_index]
        sel.annotation.set_text(f'Date: {x_date}\nPrice: {y:.2f}\n{sma_periods_short}-Day SMA Slope: {slope_short_at_hover:.2f}\n{sma_periods_long}-Day SMA Slope: {slope_long_at_hover:.2f}')
        sel.annotation.set_bbox(dict(boxstyle="round,pad=0.5", edgecolor="black", facecolor="lightblue", alpha=0.8))

    # Use tight_layout to automatically adjust subplot parameters to give specified padding
    plt.tight_layout()