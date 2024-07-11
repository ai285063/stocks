# Stocks

Some stock indicators I would like to use to monitor the stock market.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ai285063/stocks.git
   ```

2. Install dependencies
   ```sh
   pip3 install -r requirements.txt
   ```

3. Setup config.json
   1. create a file `config.json` and copy content from `config.json.example`
   2. modify variables as desired
   3. Delete lines that start with `//` in `config.json` file (they are just guidelines)
   * Find company stock symbols on this [website](https://finance.yahoo.com/lookup/)


## Usage

1. Start the project by
   ```sh
   python3 main.py
   ```

2. What will happen?
   1. matplotlib will pop out and show graphs
   2.  `htmlFiles` folder will be created, storing html files of tables that show intersections of the selected stocks
   3. a browser will open automatically and show the html file


