s=input('enter the string')
words=s.split()
l=[]
for word in words:
	words[0][0],words[0][-1]=words[0][-1],words[0][0]
print('The resultant string is:',words)
