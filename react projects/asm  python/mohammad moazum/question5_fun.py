def inte(a):
	l=[]
	i=0
	while i < a:
		d=int(input('Enter the integers:'))
		l.append(d)
		i=i+1
	return l

def swap(s):
	i=0
	while i <n:
		s[i],s[i+1]=s[i+1],s[i]
		i=i+2
	print(s)
		
		

n=int(input('Enter the value of n:'))
y=inte(n)
print(y)
swap(y)
print(y)		
