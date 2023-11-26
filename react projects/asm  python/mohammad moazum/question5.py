n=int(input('Enter the values of n :'))
L=[]
i=0
while i<n:
	d=int(input('Enter the integers :'))
	L.append(d)
	i=i+1
print(L)
while i<n-1:
	L[i],L[i+1]=L[i+1],L[i]	
	i=i+2
print(L)	
