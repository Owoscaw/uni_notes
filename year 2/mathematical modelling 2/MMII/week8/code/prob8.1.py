from matplotlib import pyplot as plt
import numpy as np

aMax = 5
vVals = np.linspace(0, 100, 100)
carLength = 5
qVals = (2*aMax*vVals)/(vVals**2+2*carLength*aMax)

plt.plot(vVals, qVals)
plt.xlabel(r"Car speed $v_0$ ms$^{-1}$")
plt.ylabel(r"Flow rate $q$")
plt.title("Flow rate against car speed")
plt.show()