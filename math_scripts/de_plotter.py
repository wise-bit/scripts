import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

def heaviside(x):
    if x < 0: return 0
    elif x == 0: return 0.5
    return 1

# function that returns dy/dt
def model(y, t):
    w = 2 * math.pi * 60
    Vrms = 120
    L = 0.006

    dydt = (heaviside(t) * (2**0.5) * Vrms * math.cos(w * t)) * (1/L) - y*(0.05/L)
    return dydt

# initial condition
y0 = 5

# time points
t = np.linspace(0,20)

# solve ODE
y = odeint(model,y0,t)

# plot results
plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()


## ---------------------

# Multiple graphs

# def f(s,t):
#     a = 4
#     b = 7
#     n = s[0]
#     c = s[1]
#     dndt = a * n - (c/(c+1)) * b * n
#     # dcdt = 1
#     return [dndt]

# t = np.linspace(0,20)
# s0=[20,5]

# s = odeint(f,s0,t)

# plt.plot(t,s[:,0],'r--', linewidth=2.0)
# plt.plot(t,s[:,1],'b-', linewidth=2.0)
# plt.xlabel("t")
# plt.ylabel("S[N,C]")
# plt.legend(["N","C"])
# plt.show()


