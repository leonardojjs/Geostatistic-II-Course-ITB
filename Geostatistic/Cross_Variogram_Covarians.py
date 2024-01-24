import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Data Well 34-29.xlsx')

dfData = df['Log Permeability']
dfData1 = df['Porosity (%)']

def cross_covarians_lag(x) :
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    for i in range (len(dfData)-x) :
        sum_xy = sum_xy + (1/(len(dfData)-x))*(dfData1[i]*dfData[i+x])
        sum_x = sum_x + (1/(len(dfData)-x))*(dfData1[i])
        sum_y = sum_y + (1/(len(dfData)-x))*(dfData[i+x])
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