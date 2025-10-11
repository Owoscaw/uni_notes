import time as t
import tkinter as tk

class BallAndBox():
    __state = []
    __size = 0

    def __init__(self, size):
        self.__size = size
        self.__state = [0]*size

    def get_state(self):
        return self.__state
    
    def set_state(self, state):
        self.__state = state

    def evolve(self):
        for i in range(self.__size):
            if self.__state[i] == 1:
                updated_index = self.__get_next_cell(i)
                self.__state[i] = 0
                self.__state[updated_index] = 2

        self.__state = [0 if box == 0 else 1 for box in self.__state]
                

    
    def __get_next_cell(self, index):
        for i in range(self.__size):
            if self.__state[(i + index)%self.__size] == 0:
                return (i + index)%self.__size
        return None
    

def run_simulation(model, sim_time):
    for i in range(sim_time):
        model.evolve()
        print(model.get_state())

test = BallAndBox(10)
test.set_state([0,0,1,1,1,0,0,1,0,1])
run_simulation(test, 10)