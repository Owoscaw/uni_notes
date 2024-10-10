import numpy as np

def swap_odd_even(array):
    if len(array)%2 != 0:
        return []
    result = [0]*6
    odds = array[::2]
    evens = array[1::2]
    result[1::2] = odds
    result[::2] = evens
    return result

print(swap_odd_even([1,4,7,2,3,6]))