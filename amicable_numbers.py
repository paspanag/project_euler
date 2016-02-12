from itertools import combinations

def factors(n):
	return [ x for x in range(1, n) if n % x == 0 ]

def d_n(n):
	return sum(factors(n))

if __name__ == "__main__":
	amicable_sum = 0
	amicable_cache = []
	for x in range(0,10001):
		sum_d = d_n(x)
		y = d_n(x)
		y_p = d_n(y) 
		if y_p == x and x != y:
			amicable_cache.append(x)
			amicable_cache.append(y)

	print sum(set(amicable_cache))
	print set(amicable_cache)