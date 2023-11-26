l1=[10,11,12,13,14,15,16,17,18];
l2=[x  for x in l1  if x%2==0]
print('l2 is :',l2)
l3=[x+5  for x in l1  if x%2==0]
print('l3 =',l3)
l4=['123','156','15','100']
l5=[int(x) for x in l4]
print('l5=',l5)


r1=range(10)
print('r1',list(r1))
r2=range(2,10)
print('r2',list(r2))
r3=range(2,10,2)
print('r3',list(r3))
A=[0 for i in range(5)]
print('value of A',A)
