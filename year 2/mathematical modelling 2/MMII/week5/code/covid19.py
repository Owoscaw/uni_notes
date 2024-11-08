import numpy as np
import matplotlib.pyplot as plt 
from covid19_base import *

class Covid(Covid_base):

    def step(self): # Perform a single integration step
        #super().step()

        # Computing difference in new infections and recoveries
        DI = np.convolve(self.DI, self.Pi)[self.pad + self.d]
        Drd = np.convolve(self.DI, self.Pr)[self.pad + self.d]

        self.DI[self.d+self.pad] = self.Rpar*DI*self.S[self.d]/self.Pop # New delta I (change in infected)
        self.DR[self.d] = (1-self.Kf)*Drd # New delta R (change in recovered)
        self.DF[self.d] = self.Kf*Drd # New delta F (change in fatalities)
        self.S[self.d+1] = self.S[self.d]- self.DI[self.pad+self.d] # Removing the infected population from the susceptible population

        # DR and DF are no longer infected, so they are removed from the infected population while new infections are added
        self.I[self.d+1] = self.I[self.d]+ self.DI[self.pad+self.d] - self.DR[self.d] - self.DF[self.d]

        # Adding the new recoveries and fatalities to the current populations
        self.R[self.d+1] = self.R[self.d] + self.DR[self.d]
        self.F[self.d+1] = self.F[self.d] + self.DF[self.d] 

