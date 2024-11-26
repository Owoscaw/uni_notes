import traffic as tl
density = 0.4
vmax=4
road_len = 200
p_slowdown = 0.1
N = 200
Nrelax = 100
tl.simulate(density, vmax, road_len, p_slowdown, N, Nrelax, '')
tl.flow_density(0.01, 1, 100, vmax, road_len, p_slowdown, '')
