import sys
if len(sys.argv) != 4:
	print("need 3 files")
	sys.exit(1)
# matrix 1
	
matrixone = open(sys.argv[1],'r')
lines = matrixone.readlines()
matrixfirst = []

for x in lines:
	 li = x.split()
	 l = [int(y) for y in li]
	 matrixfirst.append(l)
		
print(matrixfirst)

##MATRIX 2
matrixtwo = open(sys.argv[2],'r')
lines = matrixtwo.readlines()
matrixsecond = []

for x in lines:
	 li = x.split()
	 l = [int(y) for y in li]
	 matrixsecond.append(l)
		
print(matrixsecond)
#sum of two matrix
matrixthird = []

if len(matrixfirst)==len(matrixsecond) and len(matrixfirst[0])==len(matrixsecond[0]):
	for i in range(len(matrixfirst)):
		row=[]
		for j in range(len(matrixfirst[0])):
			row.append(matrixfirst[i][j] + matrixsecond[i][j])
		matrixthird.append(row)
		
print(matrixthird)

matrixone.close()
matrixtwo.close()

fout=open(sys.argv[3],'w')
for row in matrixthird:
	L=[str(x)  for x in row]
	s=' '.join(L)
	s=s+'\n'
	fout.write(s)
fout.close()	
