r=int(input('Enter the number of rows : '))
c=int(input('Enter the number of columns: '))
m=[]
i=0
while i<r:
	row=[]
	j=0
	while j<c:
		data=int(input('Enter the data:'))
		row.append(data)
		j=j+1
	m.append(row)
	i=i+1
print(m)
print('Matrix is :')
for row in m:
	for x in row:
		print(x,' ',end='')		
	print()	
