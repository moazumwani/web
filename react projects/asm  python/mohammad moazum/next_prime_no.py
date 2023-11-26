def is_prime(m):
	if m<=1:
		return True
	for i in range(2,m):
		if m%i == 0:
			return False
	return True
def nxt_prime(m):
	while True:
		m = m+1
		r = is_prime(m)
		if r == True:
			return m 
x=int(input('Enter the number:'))
r=nxt_prime(x)				
print(x,'next prime is:', 'is', r)
		
