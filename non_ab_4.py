from itertools import combinations
from amicable_numbers import d_n
from prime_factors import prime_factor_it as primes_of

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
        if p(n) > x:
            yield x

def p(n): # n is list of factors
    n_primes = primes_of(n)

    pf_0 = None
    factor_sums = 1
    factor_acc = 1
    all_sums = []

    for prime_factor in n_primes:

        if not pf_0:
            pf_0 = prime_factor

        if prime_factor % pf_0 != 0:
            all_sums.append(factor_sums)
            pf_0 = prime_factor
            factor_acc = 1
            factor_sums = 1

        factor_sums += factor_acc*prime_factor
        factor_acc *= prime_factor

    all_sums.append(factor_sums)

    return product(all_sums) - n

def product(factors):
    return reduce(lambda x, y: x*y, factors, 1)

def is_sum_of_2_abundants(n):
    pass

if __name__ == "__main__":
    x_0 = 0
    diffs = []
    # odds = [ x for x in range(947, 20161, 2) ]
    relevant_abundants = set([ x for x in generator_ab(20161) ])
    # print p(1800)
