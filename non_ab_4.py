from itertools import combinations
from amicable_numbers import d_n
from prime_factors import prime_factor_it as primes_of
from math import sqrt

class abundant_cache(object):
	def __init__(self):
		self._cache = {}

	def __call__(self,n,n_val):
		if n not in self._cache:
			self._cache[n] = n_val
		return self._cache[n]

	def __repr__(self):
		return str(self._cache)

	def __len__(self):
		return len(self._cache)


def generator_ab(n,l=0):
    for x in range(l,l+n):
        if d(x) > x:
            yield x

def d(n):
    s = 1
    t = sqrt(n)
    for i in range(2, int(t)+1):
        if n % i == 0: s += i + n/i
    if t == int(t): s -= t    #correct s if t is a perfect square
    return s

def p(n): # n is list of factors
    n_primes = primes_of(n)

    pf_0 = None
    factor_sums = 1
    factor_acc = 1
    all_sums = 1

    for prime_factor in n_primes:

        if not pf_0:
            pf_0 = prime_factor

        if prime_factor % pf_0 != 0:
            all_sums *= factor_sums
            pf_0 = prime_factor
            factor_acc = 1
            factor_sums = 1

        factor_sums += factor_acc*prime_factor
        factor_acc *= prime_factor

    all_sums *= factor_sums

    return all_sums - n

def sums_of_abundants(abundants):
    sums_collection = { x: False for x in range(0,20162) }
    for abundant_number_a in abundants:
        for abundant_number_b in abundants:
            if abundant_number_a + abundant_number_b > 20161:
                break
            else:
                sums_collection[abundant_number_a+abundant_number_b] = True
    return sums_collection

if __name__ == "__main__":
    relevant_abundants = [ x for x in generator_ab(20161) if x != 0 ]
    index = sums_of_abundants(relevant_abundants)
    non_abundant_sums = [ x for x in range(0,20162) if not index[x] ]
    print sum(non_abundant_sums)


    # not_sure_if_sums = [ x for x in range(0,46,2) ] + [ x for x in range(943, 20161, 2) ]
    # print len(not_sure_if_sums)

    # print p(1800)
