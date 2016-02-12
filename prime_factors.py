import math

def prime_factor(n, prime_list=None,  acc=None):
	# not optimized, may go up to the end of prime number list, while after sqrt(n), there
	# can only be on prime number
	prime_list = prime_list if prime_list is not None else sieve_of_e_it(n)
	acc = acc if acc is not None else []
	if len(prime_list) == 0:
		return sorted(acc)
	elif n % prime_list[0] == 0:
		acc.append(prime_list[0])
		return prime_factor(n/prime_list[0], prime_list, acc)
	else:
		return prime_factor(n, prime_list[1:], acc)

def prime_factor_it(n,prime_list=None):
	acc = []
	n_cur = n
	prime_list = prime_list if prime_list is not None else sieve_of_e_it(int(math.sqrt(n))+1)
	x = 0

	while True:
		try:
			current_prime = prime_list[x]
		except IndexError:
			break

		if current_prime > math.sqrt(n):
			break
		
		if n_cur % current_prime == 0:
			acc.append(current_prime)
			n_cur = n_cur/current_prime
		else:
			x += 1
	
	if n_cur > 2:
		acc.append(n_cur)
	
	return acc
		
def sieve_of_eratosthenes(n, n_cur=2, collector=None):
	collector = collector if collector else range(2,n+1)
	if n_cur >= n:
		return collector
	else:
		return sieve_of_eratosthenes(n, n_cur+1,[ x for x in collector if x == n_cur or x % n_cur != 0])

def sieve_of_e_it(n):
	nums = tuple(range(2,n+1))
	is_composite = [False] * len(nums)
	
	for x in range(0, len(nums)):
		cur_num, cur_status = nums[x], is_composite[x]
		if not cur_status:
			for y in range(x+1, len(nums)):
				other_num, other_stat =  nums[y], is_composite[y]
				if not other_stat and other_num % cur_num == 0:
					is_composite[y] = True
	return [ nums[x] for x in range(0, len(nums)) if not is_composite[x] ]
	
	
		

def sieve_of_atkin():
	pass

if __name__ == "__main__":
	import sys
	sys.setrecursionlimit(20000)
	print prime_factor_it(75321113)
	print prime_factor(75321113)
	
	#print sieve_of_e_it(75000)