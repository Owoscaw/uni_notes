import numpy as np
import matplotlib.pyplot as plt 
from covid19_base import *

class Covid(Covid_base):

    def step(self): # Perform a single integration step
        super().step()
