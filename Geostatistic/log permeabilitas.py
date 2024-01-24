import pandas as pd
import matplotlib.pyplot as plt
import statistics

y = pd.read_excel("Gas.xlsx", sheet_name="y")

logpm = []
for i in y.index:
    data = {}
    data = y['logpm'][i]
    logpm.append(data)


mean_logpm = statistics.mean(logpm)

def cov_with_lag(x) :
    cov = 0
    for i in range (len(logpm)-x) :
        cov = cov + (1/(len(logpm)-x))*(logpm[i]*logpm[i+x])
    return cov-(mean_logpm)**2


lag = []
covarians = []
coef_correl = []
variogram = []

for i in range (29):
    lag.append(i)
    covarians.append(cov_with_lag(i))
    coef_correl.append(cov_with_lag(i)/cov_with_lag(0))
    variogram.append(cov_with_lag(0)-cov_with_lag(i))

print("Covariansi dengan lag 0 sampai 28 : ", covarians)
print("Koefisien Korelasi dengan lag 0 sampai 28 : ", coef_correl)
print("Variogram dengan lag 0 sampai 28 : ", variogram)

fig, ax = plt.subplots(2)
ax[0].set_ylabel('Kovariansi')
ax[0].tick_params(axis='y', colors='green')
ax[0].plot(lag,covarians,'og-')
ax2 = ax[0].twinx()
ax2 = plt.gca()
ax2.set_ylabel('Koefisien Korelasi')
ax2.tick_params(axis='y', colors='red')
ax2.set_ylim(-0.5,1.5)
ax2.plot(lag,coef_correl,'xr-')

ax[1].set_ylabel('Kovariansi')
ax[1].set_xlabel('Jarak Lag')
ax[1].tick_params(axis='y', colors='blue')
ax[1].plot(lag,covarians,'ob-')
ax3 = ax[1].twinx()
ax3.set_ylabel('Variogram')
ax3.tick_params(axis='y', colors='red')
ax3.plot(lag,variogram,'xr-')
plt.show()
