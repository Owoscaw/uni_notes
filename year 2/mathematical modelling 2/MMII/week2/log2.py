import matplotlib.pyplot as plt

R = [2.5, 2.8, 3.2, 3.4, 3.5, 3.9]
N = 0.5

for r in R:
    t_list = []
    N_list = []
    for t in range(101):
        t_list.append(t)
        N_list.append(N)
        N = r*N*(1-N)

    plt.plot(t_list, N_list, ".")


plt.ylabel("$N_{t}$")
plt.xlabel("$t$")
plt.show()