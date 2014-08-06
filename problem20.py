fact=1
for x in xrange(1,100):
	fact=fact*x
sum=0
while fact>0:
	sum=sum+(fact%10)
	fact=fact/10
print sum