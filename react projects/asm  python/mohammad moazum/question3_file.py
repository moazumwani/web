fin1=open('temp2.dat','r')

l1=[]
while True:
	line1=fin1.readline()
	if len(line1)==0:
		break
	l1.append(line1)
fin1.close()
	
fin2=open('temp1.dat','r')
l2=[]
while True:
	line2=fin2.readline()
	if len(line2)==0:
		break
	l2.append(line2)
fin2.close()	

n1=len(l1)
n2=len(l2)	
if n1!= n2:
	print('different')
	exit()
	
i=0
while i<n1:
	if l1[i] != l2[i]:
		print('different')
		exit(1)
	i=i+1
print('same')
exit(0)
			

