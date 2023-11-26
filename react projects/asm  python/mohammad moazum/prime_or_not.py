def is_prime(m):
	if m<=1:
		return True
	for i in range(2,m):
		if m%i==0:
			return False
	return True

x=int(input('Enter the number:'))
r=is_prime(x)
if r==True:
	print(x,'is prime')
else:
	print(x,'is not prime')
