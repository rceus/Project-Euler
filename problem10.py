#Taking too much time N^2
#Function to calculate primes till upperbound
"""
def primes(upperbound):
	prime=2
	while prime<upperbound:
		flag=0
		for i in range(2,prime):
			if prime%i==0:
				flag=1
		if flag==0:
			yield prime
		prime=prime+1
print sum(primes(10))
"""

