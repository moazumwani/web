s=input('Enter the string :')
words=s.split()
l=[]
d={}
for word in words:
	if word not in d:
		d[word]=1
	else:
		d[word]=d[word]+1		
for k in d:
	print(k,'-->',d[k])		
