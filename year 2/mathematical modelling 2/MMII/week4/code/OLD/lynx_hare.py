import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read in the data, using the 'Year' column (column 0) as
# the index to access things later
data = pd.read_csv('data/hare_lynx_data.csv', index_col=0)

# To restrict to a subset of years, use e.g.
# data = data[data.index>=1919]  

plt.plot(data.index, data["Lynx"].values, 'ro-')
plt.plot(data.index, data["Hare"].values, 'bo-')
plt.legend(['Lynx', 'Hare'])
plt.show()

plt.plot(data["Hare"].values, data["Lynx"].values, 'bo');
plt.xlabel("hare")
plt.ylabel("lynx")
plt.show()
