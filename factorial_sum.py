def factorial(n, product=1):
	if n == 1:
		return product
	else:
		return factorial(n-1, product*n)

def factorial_digits(n, digits = []):
	if n == 0:
		return digits
	else:
		digits.append(n % 10)
		return factorial_digits(n/10, digits)

if __name__ == "__main__":
	print sum(factorial_digits(factorial(100)))