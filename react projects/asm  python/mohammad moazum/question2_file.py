fin=open('temp.txt','r')
count=0
while True:
	line=fin.readline()
	
	if len(line)==0:
		break
	words=line.split()
	n=len(words)
	count=count+n
print(count)
fin.close()	
