def even(s):
	count=0
	words=s.split()
	for word in words:
		n=len(word)
		r=n%2
		if r==0:
			count=count+1
	print('number of even words',count)

s=input('enter some string')
even(s)			
