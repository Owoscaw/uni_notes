import gravity as gr
import math
import numpy as np
import matplotlib.pyplot as plt
from spacecraft import *

thrustvals = []
colours = ["r", "g"]

for colour in colours:
  dt = 0.1
  gdt = 1
  s = Spacecraft([0,0,0,0],dt,0,4e5,4000.) # initial condition set later
  tmax= 4000

  try:
    Fr = float(input("F_r:    "))
    Ftheta = float(input("F_theta:    "))
    t_thrust = float(input("t_thrust:    "))
  except:
    break
   
  thrustvals.append(t_thrust)

  tmin,dmin = s.min_dist_to_target(Fr,Ftheta,t_thrust,tmax,dt,gdt)
  print("Fr={} Ftheta={} t_thrust={}".format(Fr,Ftheta,t_thrust))
  print("dmin={}, tmin={} Fuel={}"\
    .format(dmin,tmin,(abs(Fr)+abs(Ftheta))*t_thrust))
  s.plot(1,3,'%s-'%(colour))
  plt.xlabel(r'$\phi$',fontsize=15)
  plt.ylabel(r'$z$',fontsize=15)

  #plt.plot([0],[0],'r+', label=r'$t_\text{min}\approx$ %s, $d_\text{min}\approx$ %s'%(round(tmin, 2), round(dmin, 2)))
  #plt.title(r'Orbital parameters: $F_r=$ %s, $F_\theta=$ %s, $t_\text{thrust}=$ %s'%(Fr, Ftheta, t_thrust))

  #plt.plot([0],[0], '%s+'%(colour), label=r'$t_\text{min}\approx$ %s, $d_\text{min}\approx$ %s, $t_\text{thrust}=$ %s'%(round(tmin,2), round(dmin,2), t_thrust))
  #plt.title(r'Direct path orbit varying $t_\text{thrust}$')
  
  plt.plot([0],[0], '%s-'%(colour), label=r'''$t_\text{min}\approx$ %s, $d_\text{min}\approx$ %s, $F_r=$ %s,
            $t_\text{thrust}=$ %s, Fuel = %s'''%(round(tmin, 2), round(dmin, 2), Fr, t_thrust, (abs(Fr) + abs(Ftheta))*t_thrust))

plt.plot([0],[0], "r+")
plt.legend(loc="best")
plt.title("Close orbits")
plt.show()
