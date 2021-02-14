import yfinance as yf
import os

symbols = ['MMM', 'ABT', 'ABBV']

symbols.append('SPY')

if not os.path.exists('data'):
    os.mkdir('data')

for symbol in symbols:
    if not os.path.exists(f"data/{symbol}.csv"):
        data = yf.download(symbol, start="2010-01-01", end="2018-12-31")
        if data.size > 0:
            data.to_csv(f"data/{symbol}.csv")
        else:
            print("Not saving...")
            
for symbol in symbols:
    s = open(f"data/{symbol}.csv").readlines()
    if len(s) < 10:
        os.system(f"rm data/{symbol}.csv")