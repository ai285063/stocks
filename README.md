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
   i. create a file `config.json` and copy content from `config.json.example`
   ii. modify variables as desired
   iii. delete lines starts with `//` in the json file(those are just for guideline)


## Usage

1. Start the project by
   ```sh
   python3 main.py
   ```

2. What will happen?
   i. matplotlib will pop out and show graphs
   ii.  `htmlFiles` folder will be created, storing tables of intersection of the selected stocks
   iii. a browser will open automatically and show the html file


