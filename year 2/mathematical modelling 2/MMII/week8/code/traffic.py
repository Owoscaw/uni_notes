import tools_array as tools
import random as r
import numpy as np
from matplotlib import pyplot as plt


class Road:
    """
    Class Road : Class to simulate road at a given iteration

    :public variable : array, used to store road state
    :public variable : actualdensity, the actual density of the road
    :public variable : road_len, length of the road
    :public variable : p_slowdown, the probability a car slows down randomly
    :public variable : vmax, the legal maximum speed on the road
    :public variable : iterations, the number of iterations performed on the model
    :public variable : flow, the amount of cars that have passed the end 
                       of the road
    :public variable : isRelaxed, used to determine if one should count iterations and flow

    :public method : __init__, initialiser function
    :public method : iterate, used to step the model forward
    :public method : findHeadway, used to find the distance between one car and the next
    :public method : getFlowRate, used to find flow rate of the model
    """

    array = []
    actualdensity = 0
    road_len = 0
    p_slowdown = 0
    vmax = 0
    iterations = 0
    flow = 0
    isRelaxed = False

    def __init__(self, density, vmax, road_len, p_slowdown, isRelaxed):

        # Randomly initialising the road
        self.array, self.actualdensity = tools.fill_road_randomly(road_len, density, vmax)
        self.road_len = road_len
        self.p_slowdown = p_slowdown
        self.vmax = vmax
        self.isRelaxed = isRelaxed


    def iterate(self):
        """
        Method iterate, used to step the model forward one iteration

        :variable : accel, used to accelerate each car until it is going vmax
        :variable : decel, used to prevent a car from crashing into the next one
        :variable : rDecel, used to implement random deceleration
        :variable : newPos, used to update the positions
        :variable : passedCars, used to determine flow rate
        """

        # Cars accelerate until they reach vmax
        accel = [min(v + 1, self.vmax) if v != -1 else -1 for v in self.array]

        # Cars decelerate if they would otherwise hit another car
        decel = [min(accel[pos], self.findHeadway(pos) - 1) if accel[pos] != -1 else -1 for pos in range(self.road_len)]
        
        rDecel = [-1]*self.road_len
        newPos = [-1]*self.road_len
        passedCars = 0
        
        for pos in range(self.road_len):
            if decel[pos] == -1:
                rDecel[pos] = -1
                continue
            
            # Randomly slow down the car according to parameter
            if r.random() < self.p_slowdown:
                rDecel[pos] = max(decel[pos] - 1, 0)
            else:
                rDecel[pos] = decel[pos]

        # Update car positions, as well as keeping track of passed cars
        for pos in range(self.road_len):
            if self.array[pos] == -1:
                continue
            if pos + rDecel[pos] >= self.road_len:
                passedCars += 1
            newPos[(pos + rDecel[pos])%self.road_len] = rDecel[pos]

        self.array = newPos.copy()

        # Keeping track of flow and iterations when system is relaxed
        if self.isRelaxed:
            self.iterations += 1
            self.flow += passedCars


    def findHeadway(self, position):
        """
        Function findHeadway, determines the distance between the car at position and the next

        :param : position, the position of the car

        :variable : currentPos, used to keep track of the current position after the car given by position
        """

        # Next car must be AFTER current car
        position += 1
        for n in range(self.road_len):
            currentPos = (position + n)%self.road_len
            if self.array[currentPos] != -1:

                return n + 1
        return -1
    
    def getFlowRate(self):
        return (self.flow / self.iterations, self.actualdensity)
    

def simulate(density, vmax, road_len, p_slowdown, N, Nrelax, filename):
    """
    Function simulate, used to perform a road simulation

    Parameters explained in sheet.
    """

    # Initialising road state
    road = Road(density, vmax, road_len, p_slowdown, False)

    # Getting system into equilibrium
    for i in range(Nrelax):
        road.iterate()

    # Set isRelaxed to true, so starting to keep track of flow
    road.isRelaxed = True
    data = []
    for i in range(N):
        road.iterate()
        data.append(road.array)

    #tools.make_plot(data, road.actualdensity, vmax, road_len, filename)
    return road


def flow_density(dmin, dmax, Nd, vmax, road_len, p_slowdown, filename):
    """
    Method flow_density, used to compare flow against density

    Parameters explained in sheet.
    """

    densityVals = np.linspace(dmin, dmax, Nd)
    realDensityVals = []
    flowVals = []

    for density in densityVals:
        roadSim = simulate(density, vmax, road_len, p_slowdown, 200, 100, filename)
        flow, realDensity = roadSim.getFlowRate()
        flowVals.append(flow)
        realDensityVals.append(realDensity)

    plt.plot(realDensityVals, flowVals, "b*")
    plt.xlabel("Density")
    plt.ylabel("Flow rate")
    plt.title("Traffic flow against density, vmax={}".format(vmax))
    plt.show()

