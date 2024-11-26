import traffic as tl
density = 0.4
vmax=4
road_len = 200
p_slowdown = 0.1
N = 200
Nrelax = 100

for density in [0.1, 0.2, 0.3, 0.4, 0.5] :
  tl.simulate(density, vmax, road_len, p_slowdown, N, Nrelax,
              "Traffic_vmax{}_d{}.pdf".format(vmax,density))

for vmax in [1,2,3,4]:  
  tl.flow_density(0.01, 1, 100, vmax, road_len, p_slowdown, \
                  "FlowDensity_vmax{}.pdf".format(vmax))
