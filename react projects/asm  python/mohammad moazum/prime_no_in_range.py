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
def get_primes(m,n):
	L=[]
	for x in range(m,n):
		r=is_prime(x)
		if r==True:L.append(x)
		
	return L
def getprimes(m,n):
	L=[]
	while m<n:
		m=nxt_prime(m)
		if m>=n:
			break
		L.append(m)
	return L
x=int(input('Enter the lower bond:'))
y=int(input('Enter the upper bond :'))
primes=get_primes(x,y)				
print('prime numbers in between the:',x,y ,'are',primes)
primes=getprimes(x,y)				
print('prime numbers in between the:',x , y, 'are',primes)
		
