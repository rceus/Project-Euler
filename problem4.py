#working
temp_product=0
for x in xrange(999,100, -1):
	for y in xrange(x,100,-1):
		product=x*y
		if product>temp_product:
			if str(x*y) == str(x*y)[::-1]:
				temp_product=x*y
print temp_product