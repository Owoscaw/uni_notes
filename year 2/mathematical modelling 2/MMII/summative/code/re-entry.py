import numpy as np
import matplotlib.pyplot as plt

sigma = 7.57
B = 4.63e30
G = 6.673e-11
M_E = 5.97e24
R_E = 6370e3

heights = np.linspace(300e3, 1000e3, 100)

def get_re_entry(h, ratio):
    return (ratio*((h**(sigma + 1))/(4*(sigma + 1)*B*(G*M_E*R_E)**(1/2))))/(3.154e7)

objects = ["cube", "rod", "plate", "ship"]
m_over_A = [1e-2*2700, 50, 2*1e-3*2700, (4*3850)/(np.pi*3**2)]
style = ["black", "green", "blue", "red"]

for i in range(4):
    plt.semilogy(heights, get_re_entry(heights, m_over_A[i]), color=style[i], label=objects[i])

plt.xlabel(r"Initial altitude, $h$, in $m$")
plt.ylabel(r"Logarithm of re-entry time, $\log(t(h))$ in years")
plt.title("Initial altitude versus re-entry time")
plt.legend()
plt.show()


