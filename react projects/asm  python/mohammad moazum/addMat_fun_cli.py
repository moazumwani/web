import sys
def matrix(a):
	fin=open(a)
	lines=fin.readlines()
	fin.close()
	m1 = []
	for x in lines:
	 	l1 = x.split()
	 	l = [int(y) for y in l1]
	 	m1.append(l)
	return m1
	
def sum(a,b):
	if len(a) == len(b) and len(a[0])==len(b[0]):
		i = 0
		temp = []
		while i < len(a):
			j = 0
			row = []
			while j<len(a[0]):
				row.append(a[i][j]  + b[i][j])
				j = j + 1
			temp.append(row)
			i = i + 1
		return temp
					
def printmatrix(a,filename):
	fout=open(filename,'w')
	for row in a:
		L=[str(x)  for x in row]
		s=' '.join(L)
		s=s+'\n'
		fout.write(s)
	fout.close()	

if len(sys.argv)!=4:
	print('give two matrices: ')
	sys.exit(1)
	
m1=matrix(sys.argv[1])
print(m1)
m2=matrix(sys.argv[2])
print(m2)
m3 = sum(m1,m2)
print(m3)
printmatrix(m3,sys.argv[3])
