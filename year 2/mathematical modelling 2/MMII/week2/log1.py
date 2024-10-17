import matplotlib.pyplot as plt
import numpy as np

R = 1.2
N = np.linspace(0, 1, 10)

for n in N:
    t_list = []
    N_list = []
    for t in range(101):
        t_list.append(t)
        N_list.append(n)
        n = R*n*(1-n)

    plt.plot(t_list, N_list, ".")


plt.ylabel("$N_{t}$")
plt.xlabel("$t$")
plt.show()