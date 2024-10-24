import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize 
import MMII.week3.code.read_covid as rc

csvData = np.genfromtxt("MMII\week3\code\Covid19_Italy_2020.csv", delimiter=",", comments="#")
days, data = zip(*rc.rem_zeros(csvData))
days = np.array(days)
data = np.array(data)
