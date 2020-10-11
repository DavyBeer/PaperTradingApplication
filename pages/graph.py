import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
import plotly.plotly as py
from matplotlib.dates import DateFormatter

tgt = yf.download('TGT', period = "ytd", interval = "1d")
wmt = yf.download('WMT', period = "ytd", interval = "1d")
kr = yf.download('KR', period = "ytd", interval = "1d")

target = tgt["Open"]
walmart = wmt["Open"]
kroger = kr["Open"]

fig, ax = plt.subplots(figsize=(19, 13), edgecolor = 'white')

ax.plot(target, 'r', label = 'TARGET', linewidth = 3)
ax.plot(walmart, 'b', label = 'WALMART', linewidth = 3)
ax.plot(kroger, 'g', label = 'KROGER', linewidth = 3)


plt.title('Target, Walmart, & Kroger 2020 Open Stocks', fontsize=42)
plt.legend(loc='center right', shadow=True, ncol=1,prop={'size': 28})
plt.xlabel('DATE', size = 36)
plt.ylabel('OPEN VALUE ($)', size = 36)
plt.yticks((np.arange(0, 180, 20)), size = 30)
plt.xticks(size = 30)
date_form = DateFormatter("%b")
ax.xaxis.set_major_formatter(date_form)
plt.show()


stock_graph = py.offline.plot(fig, auto_open = False, output_type="div")

#<div style="width:1000;height:100">
#{{ graph_div|safe }}
#</div>