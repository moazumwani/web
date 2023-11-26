s=input('enter the string')
words=s.split()
l=[]
count=0
for i in words:
	if(s.count(i)>=1 and(i not in l)):
		l.append(i)
print(' '.join(l))		
