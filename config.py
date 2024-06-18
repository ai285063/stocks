from datetime import datetime, timedelta
import datetime as dt

# Define the stock symbols and the time range for the data
stocks = ["AAPL", "NVDA", "GOOGL", "SPY", "QQQ"]

# Define the time range for the data
end_date = datetime.now().strftime('%Y-%m-%d')  # Today's date
start_date = (datetime.now() - timedelta(days=1825)).strftime('%Y-%m-%d')  # Date 5 year ago

# Define the SMA periods
num_periods_short = 50
num_periods_long = 150

def get_date_x_days_before(date_string, num_days_before):
    date_object = dt.datetime.strptime(date_string, "%Y-%m-%d")
    new_date = date_object - dt.timedelta(days=num_days_before)
    new_date_string = new_date.strftime("%Y-%m-%d")
    return new_date_string

start_date_x_days_before = get_date_x_days_before(start_date, num_periods_long*2)