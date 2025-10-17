import numpy as np

def distance(distances):
    shiftedDistances = distances[:]
    shiftedDistances[1:] = shiftedDistances[:-1]
    shiftedDistances[0] = distances[-1]
    return abs(np.array(distances) - np.array(shiftedDistances))

print(distance([10,14,30,45,53]))