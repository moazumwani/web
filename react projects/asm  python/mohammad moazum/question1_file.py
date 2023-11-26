fin=open('temp.txt','r')
count=0
while True:
	line=fin.readline()
	if len(line)==0:
		break
	count=count+1
print('numbers of line=',count)
fin.close()	
