n=int(input('Enter the value of n '))
L=[]
i=0
while i<n:
	d=int(input('Enter the integers:'))
	L.append(d)
	i=i+1
print(L)	
smallest = L[0]
for x in L[1:]:
	if x< smallest:
		smallest=x
print('The smallest interger in the list is:',smallest)		
