from math import sqrt
from decimal import *

fib_c = Decimal((1+sqrt(5))/2)
golden_ratio = Decimal((1-sqrt(5))/2)
def fib():
    f_n_1 = 1
    f_n_2 = 1
    while True:
        f_n = f_n_1 + f_n_2
        yield f_n
        f_n_2 = f_n_1
        f_n_1 = f_n

def fib_closed(n):
    return (fib_c**n - golden_ratio**n)/(fib_c - golden_ratio)


if __name__ == "__main__":
    big_num = int("9"*999)
    x = 1
    #
    # while True:
    #     if fib_closed(x) > big_num:
    #         print x
    #         break
    #     x+=1
    x = 3
    for fibo in fib():
        if fibo > big_num:
            print x
            break

        x+=1


    # other forms:
    # Fib(n-1) = floor( golden_ratio * Fib(n) + 1/2 )
    # Fib(n) = floor( fib_constant**n/ sqrt(5) + 1/2 )
