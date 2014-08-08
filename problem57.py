one=3
two=2
count=0
for x in xrange(0, 1000):
    one, two = one + two + two, one + two
    if len(str(one)) > len(str(two)):
        count = count+1
print count