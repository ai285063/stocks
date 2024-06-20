import matplotlib.pyplot as plt
from matplotlib.dates import num2date
import mplcursors
import numpy as np
from config import sma_periods_short, sma_periods_long

def draw_graph(stock_data, stock, ax):
    # Calculate the SMAs
    stock_data["SMA_short"] = stock_data["Close"].rolling(window=sma_periods_short).mean()
    stock_data["SMA_long"] = stock_data["Close"].rolling(window=sma_periods_long).mean()

    # Calculate the slopes of the SMAs
    slope_short = np.polyfit(range(sma_periods_short), stock_data["SMA_short"].dropna()[-sma_periods_short:], 1)[0]
    slope_long = np.polyfit(range(sma_periods_long), stock_data["SMA_long"].dropna()[-sma_periods_long:], 1)[0]

    # Draw the closing prices
    ax.plot(stock_data["Close"], label="Close")

    # Draw the SMAs
    ax.plot(stock_data["SMA_short"], color='green', label=f"{sma_periods_short}-Day SMA (Slope: {slope_short:.2f})")
    ax.plot(stock_data["SMA_long"], color='red', label=f"{sma_periods_long}-Day SMA (Slope: {slope_long:.2f})")

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
        x_date = num2date(x).date()  # convert x from a number to a date
        sel.annotation.set_text(f'({x_date}, {y:.2f})')
        # Set the annotation box properties
        sel.annotation.set_bbox(dict(boxstyle="round,pad=0.5", edgecolor="black", facecolor="lightblue", alpha=0.8))

    # Use tight_layout to automatically adjust subplot parameters to give specified padding
    plt.tight_layout()