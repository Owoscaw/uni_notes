import time as t


initial_state = [0,0,0,0,0,0,0,0,0]

def evolve(state):
    # perform ball and box rule
    for i in range(len(state)):
        if state[i] == 1:
            new_index = find_next_empty_box(state, i)
        
    return state

def find_next_empty_box(state, index):
    # find next empty box in state from box at index
    return state