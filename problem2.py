"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

#function to calculate all the numbers
def problem2(upperbound):
	fib1, fib2 = 0, 1
	while fib1 < upperbound:
		if not fib1 % 2:
			yield fib1
		fib1, fib2 = fib2, fib1+fib2

#sum them up
print sum(problem2(4000000)) 