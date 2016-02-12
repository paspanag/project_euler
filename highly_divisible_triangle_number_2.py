from prime_factors import prime_factor_it as primes
from collections import Counter

def find_combos(list_of_val):
	counts = Counter(list_of_val)
	return reduce(lambda x,y: x*(counts[y] + 1), counts, 1)

def triangle_closed_form(n):
	return n*(n+1)/2

def num_divisors_of_n(n):
	return find_combos(primes(n))

def coprime_method(n, cache={}):
	# n is the index of the triangular numbers
	triangle_value = triangle_closed_form(n)

	try:
		primes_n = cache[n]
	except KeyError:
		primes_n = primes(n)
	
	primes_n_1 = primes(n+1)
	cache[n+1] = primes_n_1
	
	primes_t_n = primes_n + primes_n_1
	try:
		primes_t_n.remove(2)
	except ValueError:
		pass

	cache[triangle_value] = primes_t_n

	return triangle_value, find_combos(primes_t_n), cache
	
if __name__ == "__main__":
	import pprint
	cache = {}
	for x in range(1,750000):
		tri, facts, cache = coprime_method(x,cache)
		if facts > 500:
			print "n = {2} triangle value {0} has {1} factors".format(tri, facts,x)
			break

	for x in range(1,750000):
		tri_form = triangle_closed_form(x)
		factors = num_divisors_of_n(tri_form)
		print "{0} - {1}".format(tri_form, factors)
		if factors > 500:
			break