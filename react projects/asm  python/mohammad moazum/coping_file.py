fin=open('temp.txt','r')
fout=open('temp1.dat','w')
while True:
	line=fin.readline()
	if len(line)==0:
		break
	fout.write(line)
fin.close()
fout.close()	
