def factorial(n):
	the_product = 1
	while n > 0:
		the_product *= n
		n -= 1
	return the_product
