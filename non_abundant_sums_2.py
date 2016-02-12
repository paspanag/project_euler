from amicable_numbers import d_n
from itertools import combinations

# lower limit is 20161

def sums(abundant_list):
	combos = combinations(abundant_list + abundant_list, 2)
	#print list(combos)
	return [ sum(x) for x in combos if sum(x) < 28123 ]

if __name__ == "__main__":

	#abundants_to_945 = [ x for x in range(0,945) if d_n(x) > x ]

	# all evens above 46 are abundunt sums, evens under 46 may or maybe not abundant
	# all odds below 957 are not abundant sums, for the reason that the smallest odd abundant is 945,
	# thus the smallest odd sum of 2 abundants must be 957 (945 + 12)
	# odds above 957 and before 20161 maybe sums of abundants
	# any number below 24 are non-abundant sums

	all_abundants = [ x for x in range(0,28123) if d_n(x) > x ]
	sums_of_abundants = set(sums(all_abundants))

	non_abundant_sums = set(range(0,28123)).difference(sums_of_abundants)

	print len(non_abundant_sums)
	print sum(non_abundant_sums)
