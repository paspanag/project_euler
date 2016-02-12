from prime_factors import prime_factor_it
from collections import Counter
from itertools import combinations
from math import sqrt

def find_combos(list_of_val):
	print list_of_val
	counts = Counter(list_of_val)
	return reduce(lambda x,y: x*(counts[y] + 1), counts, 1)

def combinatorial_form(n):
	return(find_combos(prime_factor_it(n)))

def triangle_generator(n=1000):
	# + 1 are to include the end of the range
	current_num = 1
	cur_add = 2
	yield current_num
	for x in range(1,n):
		current_num += cur_add
		cur_add += 1
		yield current_num

def triangle_generator_2(n,k=1,acc=[0]):
	if k > n:
		return acc
	else:
		acc.append(k + acc[-1])
		return triangle_generator_2(n,k+1,acc)

def triangle_closed_form(n):
	return n*(n+1)/2

def factor_generator(n):
	factor_start = 2
	acc = [1]
	count = 0
	
	while factor_start < sqrt(n):
		if n % factor_start == 0:
			#acc.append(factor_start)
			#acc.append(n/factor_start)
			count += 2
		factor_start += 1

	#return sorted(set(acc))
	return count

def coprimes(n,cache=None):
	nth_triangle = triangle_closed_form(n)
	count_n = combinatorial_form(n)
	count_n_p_1 = combinatorial_form(n+1)
	return nth_triangle, count_n + count_n_p_1 - 1
	
if __name__ == "__main__":
	import sys
	sys.setrecursionlimit(200000)
	print "{0} has {1} factors, {2} has {3} factors".format(72, find_combos(prime_factor_it(72)), 73, find_combos(prime_factor_it(73)))
	print "{0}*{1} has {2} factors".format(72,73, find_combos(prime_factor_it(72) + prime_factor_it(73)))
	print "{0} has {1} factors".format(triangle_closed_form(72),combinatorial_form(triangle_closed_form(72)))
	print prime_factor_it(76576500)
	print combinatorial_form(76576500)
	cache = {}
	for x in range(0,100):
		#triangle, factors = coprimes(x)
		if x ==  72:
			pass
			#print "{0}th triangle number = {1}, with factor count {2}".format(x, triangle, factors)

	import pprint
	#pprint.pprint(cache)
