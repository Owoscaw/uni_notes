import matplotlib.pyplot as plt

t_list = []
N_list = []
R = 3
N = 2

for t in range(51):
    if N >= 1000:
        break
    t_list.append(t)
    N_list.append(N)
    N = R*N

plt.semilogy(t_list, N_list, "b-")
plt.ylabel("$N_{t}$")
plt.xlabel("$t$")
plt.savefig("pop2.pdf")
plt.show()