#working
import time
start=time.time()
sumsquare=0
squaresum=0
temp=0
for x in xrange(1,101):
	tempx=x*x
	sumsquare=sumsquare+tempx
	squaresum=squaresum+x
squaresum=squaresum*squaresum
print squaresum-sumsquare 
elapsed=(time.time()-start)
print elapsed