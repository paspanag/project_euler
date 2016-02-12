from amicable_numbers import d_n
from itertools import combinations

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

def is_abundant(n):
	return True if d_n(n) > n else False

def abundant_generator(n, cache, l=0):
	for x in range(l,l+n):
		abundance = cache(x,is_abundant(x))
		if abundance:
			yield x


def is_abundant_sum(n, abundants, cache):
	if n % 2 == 0 and n > 46:
		return True, abundants, cache
	if n < 945 and n % 2 == 1:
		return False, abundants, cache
	elif n < 24:
		return False, abundants, cache
	elif n in [ 26, 28, 34, 46 ]:
		return False, abundants, cache
	else:
		if n > abundants[-1]:
			max_abundant = abundants[-1]
			abundants = abundants + list(abundant_generator(100, cache, l=max_abundant))
		sums = [ n - x for x in abundants ]
		for x in sums:
			abundance = cache(x,is_abundant(x))
			if abundance:
				return True, abundants, cache
		return False, abundants, cache

if __name__ == "__main__":


	# all evens above 46 are abundunt sums, evens under 46 may or maybe not abundant
	# all odds below 957 are not abundant sums, for the reason that the smallest odd abundant is 945,
	# thus the smallest odd sum of 2 abundants must be 957 (945 + 12)
	# odds above 957 and before 20161 maybe sums of abundants
	# any number below 24 are non-abundant sums

	a_cache = abundant_cache()
	abundants = list(abundant_generator(1000,a_cache))
	# sum_of_abundants = [ 945 + x for x in abundants ]
	# print sum_of_abundants
	non_abundant_sums = []
	for x in range(0, 10000):
		abundance, abundants, a_cache = is_abundant_sum(x, abundants, a_cache)
		if not abundance:
			non_abundant_sums.append(x)
	print non_abundant_sums
	print sum(non_abundant_sums)



	# numbers_below_20161 = [x for x in range(0,20161) ]
	# odds_above_945 = [x for x in range(945, 20163,2)]
	# # cache is tuple, first is the cache set, second is the highest value in the cache
	#
	# odds_less_945 = [ x for x in range(1,945,2) ]
	# evens_less_46 = [ x for x in range(0,46,2) ]
