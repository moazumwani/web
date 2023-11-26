def inte(a):
	l=[]
	i=0
	while i < a:
		d=int(input('Enter the integers:'))
		l.append(d)
		i=i+1
	return l
	while i <n:
		l[i],l[i+1]=l[i+1],l[i]
		i=i+2
	return l
	

		

n=int(input('Enter the value of n:'))
s=inte(n)
print(s)

	
		
