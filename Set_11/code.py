import matplotlib.pyplot as plt
import numpy as np

def load_dat_file(filepath, usecols=None):
    data = []
    with open(filepath, 'r') as file:
        for line in file:
            if line.strip():
                tokens = line.strip().split()
                selected = [float(tokens[i]) for i in usecols] if usecols else [float(token) for token in tokens]
                data.append(selected)
    return data

price_data = load_dat_file("SET_11/price.dat", usecols=[1, 2])
fluct_data = load_dat_file("SET_11/fluct.dat", usecols=[1, 2])
gauss_data = load_dat_file("SET_11/gauss.dat", usecols=[1, 2])
wiene_data = load_dat_file("SET_11/wiene.dat", usecols=[0, 2, 3])
trade_data = load_dat_file("SET_11/trade.dat", usecols=[1, 2])



price_time, price_val = zip(*price_data)
fluct_time, fluct_val = zip(*fluct_data)
gauss_fluct, gauss_freq = zip(*gauss_data)
wiene_time, wiene_log, wiene_var = zip(*wiene_data)
trade_time, trade_vol = zip(*trade_data)

# Figure 1
S_0= 800
a=0.0005
S_values= [S_0*np.exp(a*t) for t in price_time]

plt.figure(figsize=(10, 5))
plt.semilogy(price_time, price_val, color='hotpink')
plt.semilogy(price_time, S_values, color='black',linestyle='--')
plt.title("Fig. 1: Daily Average Price vs Time")
plt.xlabel("Time (Days)")
plt.ylabel("Daily Avg Price")
plt.grid(True)
plt.show()


# Plot Fig. 2
plt.figure(figsize=(10, 5))
plt.plot(fluct_time, fluct_val, color='crimson')
plt.title("Fig. 2: Daily % Fluctuation vs Time")
plt.xlabel("Time (Days)")
plt.ylabel("Daily % Fluctuation")
plt.grid(True)
plt.show()

# Plot Fig. 3
f0=20
mu=0.057
sigma=1.495

F_values=[1 + f0*np.exp(-((delta-mu)**2)/(2*sigma**2)) for delta in gauss_fluct]
plt.figure(figsize=(10, 5))
plt.plot(gauss_fluct, gauss_freq, color='darkblue')
plt.plot(gauss_fluct, F_values, color='yellow',linestyle='--')
plt.title("Fig. 3: Frequency of % Fluctuations")
plt.xlabel("Daily % Fluctuation")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Plot Fig. 4
S_0= 850
a=0.01
S_values= [S_0*np.exp(a*t) for t in wiene_time]
plt.figure(figsize=(10, 5))
plt.plot(wiene_time, wiene_log, color='purple')
plt.plot(wiene_time,np.log( S_values), color='black',linestyle='--')
plt.title("Fig. 4: Log(Stock Price) vs Time")
plt.xlabel("Time (Months)")
plt.ylabel("log(Price)")
plt.grid(True)
plt.show()

# Plot Fig. 5
w=-3.41*(1e-6)
Var_values=[w*tau+0.00125 for tau in wiene_time]
plt.figure(figsize=(10, 5))
plt.plot(wiene_time, wiene_var, color='red')
plt.plot(wiene_time, Var_values, color='royalblue',linestyle='--')
plt.title("Fig. 5: Wiener Variance vs Time")
plt.xlabel("Time (Months)")
plt.ylabel("Wiener Variance")
plt.grid(True)
plt.show()


# Plot Fig. 6
N_0= 35
v=0.0004
S_values= [N_0*np.exp(v*t) for t in trade_time]
plt.figure(figsize=(10, 5))
plt.plot(trade_time, trade_vol, color='darkkhaki')
plt.plot(trade_time, S_values, color='rebeccapurple',linestyle='--')
plt.title("Fig. 6: Daily Trade Volume vs Time")
plt.xlabel("Time (Days)")
plt.yscale('log')
plt.ylabel("Trade Volume")
plt.grid(True)
plt.show()