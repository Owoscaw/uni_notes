import matplotlib.pyplot as plt 
import numpy as np
import scipy
from code.ode_rk4 import ODE_RK4
from lotka_volterra import LotkaVolterra
from lotka_volterra_rk4 import LotkaVolterraRK4


# Compare accuracy of Euler and RK4 integration method
# Compute a reference solution using RK4 and a small dt
tmax=1
lv = LotkaVolterraRK4(V0=[0.1,0.1],dt=1e-5)  # Create a RK4 LV object
lv.K = 1                  # Set the parameter
lv.iterate(tmax, 0.1)     # Compute reference value
V_ref = lv.V              # Make copy of reference function values 
print("REF: t="+str(lv.t))

lve = LotkaVolterra()     # LV for Euler method
lve.K = 1

data = [[0.2, 0, 0], [0.1, 0, 0], [0.05, 0, 0], [0.02, 0, 0], [0.01, 0 , 0]] #Integration steps

# Scan a range of integration time steps
for dt in data :
  lv.reset(V0=[0.1,0.1], dt=dt[0])            # Solve LV using RK4
  lv.iterate(tmax,0.1)
  V = lv.V
  dt[1] = np.sqrt((V_ref - V).dot(V_ref-V)) #Storing RK4 error
  print("RK4 : dt="+str(dt[0])+": Error =", dt[1]) 
  #print("t="+str(lv.t))
  lve = LotkaVolterra(V0=[0.1,0.1], dt=dt[0]) # Solve LV using Euler
  lve.K = 1               
  lve.iterate(tmax,0.1)
  V = lve.V
  # Compare the errors using V_ref as reference solution
  dt[2] = np.sqrt((V_ref-V).dot(V_ref-V)) #Storing Euler error
  print("Euler dt="+str(dt[0])+": Error =", dt[2]) 
  #print("t="+str(lv.t))
  print("")

# There is probably a smarter way to do this...
dtVals = np.array([dt[0] for dt in data])
RK4Vals = np.array([dt[1] for dt in data])
EulerVals = np.array([dt[2] for dt in data])

# Fitting equation to linear function
def linFunc(x, a, b):
  return a + b*x

RK4Popt, RK4Pcov = scipy.optimize.curve_fit(linFunc, np.log(dtVals), np.log(RK4Vals), p0=[1,1])
EulerPopt, EulerPcov = scipy.optimize.curve_fit(linFunc, np.log(dtVals), np.log(EulerVals), p0=[1,1])

print(RK4Popt[1], EulerPopt[1])