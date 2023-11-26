fin=open('temp.txt','r')

l=[]
while True:
	line=fin.readline()
	
	if len(line)==0:
		break
	l.append(line)
		
	if len(line)==1:
		#print('hi')
		l.remove(line)	
		
print(l)
fin.close() 
fout=open('temp.txt','w')
fout.writelines(l)
fout.close()
