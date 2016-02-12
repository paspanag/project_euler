import math
import itertools

import math
import itertools

def find_value(m,n):
    # Used Euclid's formula for Pythagorean triples
    # from the problem assumption a + b + c = 1000
    return m * (m + n) == 500 and m > n

def generate(m,n):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return a,b,c

def is_right_triple(a,b,c):
    return a + b + c == 1000

if __name__ == '__main__':
    for m,n in itertools.permutations(range(1,100), 2):
        if find_value(m,n):
            print("a + b + c = 1000 where a = {0}, b = {1}, c = {2}".format(*generate(m,n)))
            break
