import sys
if len(sys.argv)!=3:
	print(' I need 2 inputs')
	exit(1)
x=int(sys.argv[1])
y=int(sys.argv[2])
z=x+y
print('sum =',z)	
