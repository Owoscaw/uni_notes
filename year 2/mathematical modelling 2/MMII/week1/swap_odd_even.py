
def swap_odd_even(array):
    if len(array)%2 != 0:
        return
    result = []
    evens = array[0:-1:2]
    odds = array[1:0:2]
    result.append([evens, odds])
    return result

print(swap_odd_even([1,4,7,2,3,6]))