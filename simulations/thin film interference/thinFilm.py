import numpy as np
import pygame

class Film:

    def __init__(self, refIndex=1.0, tStep=1.0, aStep=1):
        self.refIndex = refIndex
        self.tStep = tStep
        self.x, self.y = np.meshgrid(np.linspace(0, 1, aStep), np.linspace(0, 1, aStep))
        self.u, self.v = np.meshgrid(np.zeros(aStep), np.zeros(aStep))

if __name__ == "__main__":
    test = Film(1, 1, 50)