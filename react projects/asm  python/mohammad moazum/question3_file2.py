def get_lines(file_name):
	fin=open(file_name,'r')
	l=[]
	while True:

		line=fin.readline()
		if len(line)==0:
			break
		l.append(line)
	fin.close()	
	return l
	
#while True:
	#line2=fin2.readline()
	#if len(line2)==0:
	#	break
	#l2.append(line2)
l1=get_lines(fin1)
l2=get_lines(fin2)	
		
print(l1)
print(l2)	

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
fin1.close()
fin2.close()
