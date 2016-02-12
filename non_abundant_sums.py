from amicable_numbers import d_n
from itertools import combinations

# lower limit is 20161


if __name__ == "__main__":
	abundants = set([ x for x in range(0, 47) if d_n(x) > x ])
	odds_under_945 = set([ x for x in range(0, 945) if x % 2 == 1 ])
	evens_under_945 = set([ x for x in range(0, 945) if x % 2 == 0 ])
	
	sums_of_abundants = sorted(set([ sum(x) for x in combinations(abundants,2) if sum(x) < 945]))
	#numbers_under_945 = odds_under_945.union(evens_under_945.difference(sums_of_abundants))
	#print numbers_under_945
	
	even_maybe_not_sums_of_non_abundant = set([ x for x in range(0,47) if x % 2 == 0 ])
	even_sum_of_non_abundants = even_maybe_not_sums_of_non_abundant.difference(sums_of_abundants)
	print sorted(even_sum_of_non_abundants)

	odds_over_945 = set([ x for x in range(945, 20162) if x % 2 == 1])
	print len(odds_over_945)

	print sorted(set([x for x in range(0,20161) if d_n(x) == x ]))