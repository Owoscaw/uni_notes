
import spins_1d as spins
import numpy as np

sp = spins.Spins_1d(1000, J=1.0, h=0.0, f=0.2)
results = sp.simulate( np.linspace(1, 3.0, 41), 200000)
sp.plot_magnetisation(results)

sp = spins.Spins_1d(1000, J=1.0, h=0.0, f=0)
results = sp.simulate( np.linspace(1, 3.0, 41), 200000)
sp.plot_magnetisation(results)


