def inte(a):
	l=[]
	i=0
	while i < a:
		d=int(input('Enter the integers:'))
		l.append(d)
		i=i+1
	return(l)
		
def small(s):
	smallest=s[0]
	for x in s[1:]:
		if x<smallest:
			smallest =x
	return smallest
	
			
n=int(input('Enter the value of n:'))
y=inte(n)
print(y)
m=small(y)
print('The Smallest Number is :',m)
	
