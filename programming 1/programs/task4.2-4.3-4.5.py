from matplotlib import pyplot as plt
from math import log

def divisors(n):
    return [i for i in range(1, n//2 + 1) if n%i == 0]

def is_perfect(n):
    return sum(divisors(n)) == n

def show_perfect(n):
    print([i for i in range(1,n) if is_perfect(i)])

def is_prime(n):
    for i in range(2,n//2 + 1):
        if n%i == 0:
            return False
    return True

def prime_factors(n):
    return [i for i in range(2,n+1) if n%i==0 and is_prime(i) for j in range(1, int(log(n,i))+1) if n% i**j == 0]

print(prime_factors(140))
