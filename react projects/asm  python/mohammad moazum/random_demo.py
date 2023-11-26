import random
import sys
if len(sys.argv) !=2:
	print('I need one input from CLI')
	exit(1)
n=int(sys.argv[1])
i=0
L=[]
while i<n:
	r=random.randint(1,100)
	L.append(r)
	i=i+1
print(L)
