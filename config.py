from datetime import datetime, timedelta
import datetime as dt
import json

with open('config.json', 'r') as f:
    config = json.load(f)

# Check config.json for required fields
if (config.get("stocks") == None):
    ValueError("Stocks not found in config.json")
if (config.get("start_date") == None and config.get("end_date") == None and config.get("days_back") == None):
    ValueError("Either start_date and end_date or days_back must be provided in config.json")
if (config.get("sma_periods_short") == None or config.get("sma_periods_long") == None):
    ValueError("sma_periods_short and sma_periods_long must be provided in config.json")

# Define the stock symbols and the time range for the data
stocks = config.get("stocks")

# Define the time range for the data
end_date = datetime.now().strftime('%Y-%m-%d') if config["days_back"] else config["end_date"]
start_date = (datetime.now() - timedelta(days=config["days_back"])).strftime('%Y-%m-%d') if config["days_back"] else config["start_date"]

# Define the SMA periods
sma_periods_short = config["sma_periods_short"]
sma_periods_long = config["sma_periods_long"]

def get_date_x_days_before(date_string, num_days_before):
    date_object = dt.datetime.strptime(date_string, "%Y-%m-%d")
    new_date = date_object - dt.timedelta(days=num_days_before)
    new_date_string = new_date.strftime("%Y-%m-%d")
    return new_date_string

start_date_x_days_before = get_date_x_days_before(start_date, sma_periods_long*2)