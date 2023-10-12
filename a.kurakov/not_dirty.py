"does things"
import random
import numpy as np


DEFAUL_ACCURACY = 3

def sum_two_values(first, second):
    "sum of two values"
    return first + second

def div(x, y, accuracy):
    "divide"
    return round(x/y, accuracy)

def get_rand():
    "get random integer"
    return random.randint(1, 10)

def rand_array():
    "random array"
    a = [get_rand(), get_rand(), get_rand()]
    return np.array(a)

def main():
    "main"

main()
