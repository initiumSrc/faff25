# -*- coding: utf-8 -

import math
import numpy as np
import matplotlib.pyplot as plt 

# konstanter
sigma = 2.8 * 10**(-23) # m^2
tau = 230.0 * 10**(-6) # µs
N_naught = 1.4 * 10**20 * 10**6 # cm^-3 > m^-3
D = 8.0 * 10**(-3) # mm
La = 20.0 * 10**(-2) # cm
L = 60 * 10**(-2) # cm
c = 299792458.0 # m/s

R1 = 1.0 # reflektans 1
R2 = 0.05 # reflektans 2

tau_c = (-2.0 * L) / (c * (math.log(R1) + math.log(R2)))

N_inf = 0.01 * N_naught

V = L * math.pi * (D/2)**2

P = N_inf / tau
B = (sigma * c) / V

dt = 1*10**(-10)

V_a = math.pi * (4 * 10**(-3))**2 * La

# antal steg som krävs för att dt skall täcka 200µs
T = range(0, 2000000) 

N_arr = []
phi_arr = []
Time_arr = []

N_arr.append(0)
phi_arr.append(0)
Time_arr.append(0)

# iterera över våra tidssteg i, T_i = dt * i, och beräkna enligt ekvationssystem
# vi lagrar värden i array för att slippa göra om beräkningarna rekursivt (en sämre lösning)
# nästa värde i vår array beror av det förra, enligt ekvationssystemet.
for t in T:
    if t != len(T) - 1:
        Time_arr.append(dt * t)
        N_arr.append(N_arr[t] + (P - B * N_arr[t] * phi_arr[t] - N_arr[t]/tau) * dt)
        phi_arr.append(phi_arr[t] + (B * V_a * N_arr[t] * (phi_arr[t] + 1.0) - phi_arr[t]/tau_c) * dt)

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(Time_arr, phi_arr)
axarr[0].set_title('PHI')
axarr[1].plot(Time_arr, N_arr)
axarr[1].set_title('N')

plt.show()
