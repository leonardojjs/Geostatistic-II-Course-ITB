import pandas as pd
import matplotlib.pyplot as plt

y = pd.read_excel("Gas.xlsx", sheet_name="y")
depth = pd.read_excel("Gas.xlsx", sheet_name="depth")

logpm = []
for i in y.index:
    data = {}
    data = y['logpm'][i]
    logpm.append(data)

d = []
for i in y.index:
    data = {}
    data = depth['depth'][i]
    logpm.append(data)

fig, ax = plt.subplots(2)
ax[0].set_ylabel('Kovariansi')
ax[0].set_xlabel('kk')
ax[0].tick_params(axis='y', colors='green')
ax[0].plot(d,logpm,'og-')