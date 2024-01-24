import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#depth = pd.read_excel("Gas.xlsx", sheet_name="depth")
pm = pd.read_excel("Gas.xlsx", sheet_name="pm")
x = pd.read_excel("Gas.xlsx", sheet_name="x")
y = pd.read_excel("Gas.xlsx", sheet_name="y")

porosity=[]
for i in x.index:
    data = {}
    data = x['porosity'][i]
    porosity.append(data)

permeability = []
for i in pm.index:
    data = {}
    data = pm['permeability'][i]
    permeability.append(data)

logpm = []
for i in y.index:
    data = {}
    data = y['logpm'][i]
    logpm.append(data)
#print(logpm[5])

def cross_covarians_lag(x) :
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    for i in range (len(logpm)-x) :
        sum_xy = sum_xy + (1/(len(logpm)-x))*(porosity[i]*logpm[i+x])
        sum_x = sum_x + (1/(len(logpm)-x))*(porosity[i])
        sum_y = sum_y + (1/(len(logpm)-x))*(logpm[i+x])
    cross = sum_xy -(sum_y*sum_x)
    return cross

lag = []
cross_kovariansi = []
cross_variogram = []

for i in range (29):
    lag.append(i)
    cross_kovariansi.append(cross_covarians_lag(i))
    cross_variogram.append(cross_covarians_lag(0)-cross_covarians_lag(i))

print("Cross Kovariansi dengan lag 0 sampai 28 : ", cross_kovariansi)
print("Cross Variogram dengan lag 0 sampai 28 : ", cross_variogram)

fig, ax = plt.subplots()
ax.set_ylabel('Cross Kovariansi')
ax.set_xlabel('Jarak Lag')
ax.tick_params(axis='y', colors='blue')
ax.plot(lag,cross_kovariansi,'ob-')
ax3 = ax.twinx()
ax3.set_ylabel('Cross Variogram')
ax3.tick_params(axis='y', colors='red')
ax3.plot(lag,cross_variogram,'xr-')
plt.show()