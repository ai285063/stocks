import matplotlib.pyplot as plt
import numpy as np
from config import num_periods_short, num_periods_long

def draw_graph(stock_data, stock, ax):
    # Calculate the SMAs
    stock_data["SMA_short"] = stock_data["Close"].rolling(window=num_periods_short).mean()
    stock_data["SMA_long"] = stock_data["Close"].rolling(window=num_periods_long).mean()

    # Calculate the slopes of the SMAs
    slope_short = np.polyfit(range(num_periods_short), stock_data["SMA_short"].dropna()[-num_periods_short:], 1)[0]
    slope_long = np.polyfit(range(num_periods_long), stock_data["SMA_long"].dropna()[-num_periods_long:], 1)[0]

    # Draw the closing prices
    ax.plot(stock_data["Close"], label="Close")

    # Draw the SMAs
    ax.plot(stock_data["SMA_short"], color='green', label=f"{num_periods_short}-Day SMA (Slope: {slope_short:.2f})")
    ax.plot(stock_data["SMA_long"], color='red', label=f"{num_periods_long}-Day SMA (Slope: {slope_long:.2f})")

    # Set the title and labels
    ax.set_title(f"{stock} Close Prices, {num_periods_short}-Day SMA & {num_periods_long}-Day SMA")
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

    # # Adjust the plot margins
    # plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, hspace=0.4)
    # Use tight_layout to automatically adjust subplot parameters to give specified padding
    plt.tight_layout()