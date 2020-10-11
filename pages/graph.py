import yfinance as yf


SPY = yf.download('SPY')
SPY.head()

SPY['Close']

SPY = yf.Ticker('SPY')
SPY_History = SPY.history(start="2020-01-01", end="2020-02-01")
SPY_History.head()

SPY.info

SPY.info['fiftyDayAverage']

data = yf.download('SPY AAPL')
data.tail()

import matplotlib.pyplot as plt
data['Close'].plot(figsize=(10, 5))

# savefig("StockImage.png", dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)

