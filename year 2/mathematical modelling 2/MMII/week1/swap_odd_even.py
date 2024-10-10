
def swap_odd_even(array):
    if len(array)%2 != 0:
        return []
    result = [0]*len(array)
    evens = array[0::2]
    odds = array[1::2]
    result = array[:-3:-1]
    return result

print(swap_odd_even([1,4,7,2,3,6]))