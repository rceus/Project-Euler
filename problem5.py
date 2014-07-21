#notworking
flag=0
num=1
while (not flag):
	temp=0
	for i in range(1,5):
		if not num%i:
			temp=1
	if not temp:
		print num
		flag=1
	num=num+1
