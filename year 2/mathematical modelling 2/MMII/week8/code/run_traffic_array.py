import traffic_array as ta
density = 0.4
vmax=4
road_len = 200
p_slowdown = 0.1
N = 200
Nrelax = 100
ta.simulate(density, vmax, road_len, p_slowdown, N, Nrelax)
ta.flow_density(0.01, 1, 100, vmax, road_len, p_slowdown, '')
