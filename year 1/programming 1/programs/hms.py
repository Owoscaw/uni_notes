
from math import floor as roundd

def diffToRound(r):
    return r - roundd(r)

def hms(time):
    return [roundd(time), roundd(diffToRound(time)*60), time*60*60 - roundd(time)*60*60 - roundd(diffToRound(time)*60)*60]
print(hms(57.2957795))